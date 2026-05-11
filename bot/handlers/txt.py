import uuid

from aiogram import Router, types, F
from aiogram.types import FSInputFile
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext

from bot.locales.index import get_texts
from bot.utils.build_pdf_name import build_pdf_name
from bot.services.txt_service import txt_to_pdf
from bot.ui.errors import send_unsupported_content
from bot.ui.navigation import return_to_main_menu
from bot.utils.files import safe_remove
from bot.utils.states import ConvertStates


router = Router()


# ---------------------------
# BACK MENU
# ---------------------------
@router.message(StateFilter(ConvertStates.convert_for_txt), F.text.contains("⬅️"))
async def back_to_menu(message: types.Message, state: FSMContext):
    await return_to_main_menu(message, state)


# ---------------------------
# TXT HANDLER
# ---------------------------
@router.message(StateFilter(ConvertStates.convert_for_txt), F.document)
async def txt_to_pdf_handler(message: types.Message):
    file_name = message.document.file_name.lower()

    if not file_name.endswith('.txt'):
        await send_unsupported_content(message)
        return

    user_id = message.from_user.id if message.from_user else 0
    operation_id = uuid.uuid4().hex[:10]

    # creating a path at the root
    input_path = f"input_{user_id}_{operation_id}.txt"
    pdf_path = build_pdf_name(user_id, operation_id)

    try:
        # 1. download images
        await message.bot.download(message.document, destination=input_path)

        # 2. convert TXT to PDF
        txt_to_pdf(input_path, pdf_path)

        # 4. send result
        await message.answer_document(FSInputFile(pdf_path))

    except Exception as e:
        print(f"TXT Error: {e}")
        lang = message.from_user.language_code if message.from_user else None
        await message.answer(get_texts(lang).PROCESSING_ERROR)

    finally:
        # cleanup
        safe_remove(input_path)
        safe_remove(pdf_path)


# ---------------------------
# FALLBACK
# ---------------------------
@router.message(StateFilter(ConvertStates.convert_for_txt))
async def txt_fallback(message: types.Message):
    await send_unsupported_content(message)
