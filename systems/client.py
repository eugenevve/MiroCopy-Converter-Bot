import os
import uuid
import img2pdf
import asyncio
from typing import Dict, List, Tuple
from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.types import BotCommand, BotCommandScopeChat, FSInputFile
from utils.messages import get_message

router = Router()

MediaGroupKey = Tuple[int, str]
media_group_photos: Dict[MediaGroupKey, List[Tuple[int, str]]] = {}
media_group_tasks: Dict[MediaGroupKey, asyncio.Task] = {}
media_group_lock = asyncio.Lock()

@router.message(Command("start"))
async def start_command(message: types.Message):
    language_code = message.from_user.language_code if message.from_user else None

    if message.from_user:
        commands = [
            BotCommand(command="start", description=get_message("command_start", language_code)),
        ]
        await message.bot.set_my_commands(commands, scope=BotCommandScopeChat(chat_id=message.from_user.id))

    await message.answer(get_message("start", language_code))

async def process_photo_batch(message: types.Message, photo_file_ids: List[str]):
    operation_id = uuid.uuid4().hex[:10]
    user_id = message.from_user.id if message.from_user else "unknown"
    temp_image_paths: List[str] = []
    pdf_path = f"result_{user_id}_{operation_id}.pdf"
    try:
        for index, file_id in enumerate(photo_file_ids, start=1):
            temp_image_path = f"temp_{user_id}_{operation_id}_{index}.jpg"
            file_info = await message.bot.get_file(file_id)
            await message.bot.download_file(file_info.file_path, temp_image_path)
            temp_image_paths.append(temp_image_path)
        with open(pdf_path, "wb") as f:
            f.write(img2pdf.convert(temp_image_paths))
        await message.answer_document(FSInputFile(pdf_path))
    except Exception as e:
        error_text = get_message("processing_error", message.from_user.language_code if message.from_user else None)
        await message.answer(error_text.format(error=e))
    finally:
        for temp_image_path in temp_image_paths:
            if os.path.exists(temp_image_path):
                os.remove(temp_image_path)
        if os.path.exists(pdf_path):
            os.remove(pdf_path)

async def flush_media_group(group_key: MediaGroupKey, message: types.Message):
    try:
        await asyncio.sleep(0.8)
    except asyncio.CancelledError:
        return
    async with media_group_lock:
        group_messages = media_group_photos.pop(group_key, [])
        media_group_tasks.pop(group_key, None)
    if not group_messages:
        return
    group_messages.sort(key=lambda item: item[0])
    file_ids = [file_id for _, file_id in group_messages]
    await process_photo_batch(message, file_ids)

@router.message(F.photo)
async def photo_to_pdf(message: types.Message):
    photo_file_id = message.photo[-1].file_id
    if not message.media_group_id:
        await process_photo_batch(message, [photo_file_id])
        return
    group_key: MediaGroupKey = (message.chat.id, message.media_group_id)
    async with media_group_lock:
        media_group_photos.setdefault(group_key, [])
        media_group_photos[group_key].append((message.message_id, photo_file_id))
        previous_task = media_group_tasks.get(group_key)
        if previous_task and not previous_task.done():
            previous_task.cancel()
        media_group_tasks[group_key] = asyncio.create_task(flush_media_group(group_key, message))

@router.message()
async def unsupported_content(message: types.Message):
    if message.photo:
        return
    await message.answer(get_message("unsupported_content", message.from_user.language_code if message.from_user else None))
