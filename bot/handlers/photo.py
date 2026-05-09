import uuid
import asyncio
from typing import Dict, List, Tuple

from aiogram import Router, types, F
from aiogram.types import FSInputFile
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext

from bot.keyboards.menu import get_menu_keyboard
from bot.locales.index import get_texts
from bot.services.pdf_service import images_to_pdf
from bot.services.file_service import download_images, build_pdf_name
from bot.ui.errors import send_unsupported_content
from bot.ui.navigation import return_to_main_menu
from bot.utils.files import safe_remove
from bot.utils.states import ConvertStates


router = Router()


MediaGroupKey = Tuple[int, str]
media_group_photos: Dict[MediaGroupKey, List[Tuple[int, str]]] = {}
media_group_lock = asyncio.Lock()


# ---------------------------
# BACK MENU
# ---------------------------
@router.message(StateFilter(ConvertStates.convert_for_photos), F.text.contains("⬅️"))
async def back_to_menu(message: types.Message, state: FSMContext):
    await return_to_main_menu(message, state)


# ---------------------------
# PHOTO HANDLER
# ---------------------------
@router.message(StateFilter(ConvertStates.convert_for_photos), F.photo)
async def photo_to_pdf(message: types.Message):
    photo_file_id = message.photo[-1].file_id

    if not message.media_group_id:
        await process_photo_batch(message, [photo_file_id])
        return

    group_key = (message.chat.id, message.media_group_id)

    async with media_group_lock:
        media_group_photos.setdefault(group_key, [])
        media_group_photos[group_key].append(
            (message.message_id, photo_file_id)
        )

    asyncio.create_task(flush_media_group(group_key, message))


# ---------------------------
# MEDIA GROUP HANDLER
# ---------------------------
async def flush_media_group(group_key: MediaGroupKey, message: types.Message):
    await asyncio.sleep(1)

    async with media_group_lock:
        messages = media_group_photos.pop(group_key, [])

    if not messages:
        return

    messages.sort(key=lambda item: item[0])
    file_ids = [file_id for _, file_id in messages]

    await process_photo_batch(message, file_ids)


# ---------------------------
# CORE PIPELINE
# ---------------------------
async def process_photo_batch(message: types.Message, photo_file_ids: List[str]):
    user_id = message.from_user.id if message.from_user else 0

    temp_image_paths = []
    pdf_path = None
    operation_id = uuid.uuid4().hex[:10]

    try:
        # 1. download images
        temp_image_paths = await download_images(
            bot=message.bot,
            file_ids=photo_file_ids,
            user_id=user_id,
            operation_id=operation_id
        )

        # 2. build pdf name
        pdf_path = build_pdf_name(user_id, operation_id)

        # 3. convert
        images_to_pdf(temp_image_paths, pdf_path)

        # 4. send result
        await message.answer_document(FSInputFile(pdf_path))

    except Exception:
        lang = message.from_user.language_code if message.from_user else None
        await message.answer(get_texts(lang).PROCESSING_ERROR)

    finally:
        # cleanup
        for path in temp_image_paths:
            safe_remove(path)

        if pdf_path:
            safe_remove(pdf_path)

# ---------------------------
# FALLBACK
# ---------------------------
@router.message(StateFilter(ConvertStates.convert_for_photos))
async def photo_fallback(message: types.Message):
    await send_unsupported_content(message)
