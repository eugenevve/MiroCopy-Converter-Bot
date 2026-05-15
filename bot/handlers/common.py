import asyncio
import datetime

from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command, CommandObject, StateFilter

from aiogram.types import ReplyKeyboardRemove
from bot.keyboards.menu import get_menu_keyboard
from bot.keyboards.back import get_back_keyboard
from bot.locales.index import get_texts
from bot.ui.errors import send_unsupported_content
from bot.utils.enums import CommandArgs
from bot.utils.states import ConvertStates


router = Router()


# ---------------------------
# START
# ---------------------------
last_starts = {}

@router.message(Command("start"))
async def cmd_start(message: types.Message, state: FSMContext, command: CommandObject):
    user_id = message.from_user.id
    now = datetime.datetime.now()

    # Problem: On Apple devices due to the way deeplinks work in the client.
    # The system may initiate a transition from inline mode twice.
    # First, a preview occurs then the actual opening resulting in two commands being sent.
    if user_id in last_starts:
        delta = (now - last_starts[user_id]).total_seconds()
        if delta < 1.0:
            return
    last_starts[user_id] = now

    if command.args == CommandArgs.IMAGE:
        return await set_image_mode(message, state)
    elif command.args == CommandArgs.TXT:
        return await set_txt_mode(message, state)
    else:
        return await show_main_menu(message, state)


async def show_main_menu(message: types.Message, state: FSMContext):
    lang = message.from_user.language_code if message.from_user else None
    await state.set_state(ConvertStates.main_menu)
    await message.answer(
        get_texts(lang).START,
        reply_markup=get_menu_keyboard(lang)
    )


# ---------------------------
# MODES
# ---------------------------
@router.message(StateFilter(ConvertStates.main_menu), F.text.contains("📸"))
@router.message(Command("image"))
async def set_image_mode(message: types.Message, state: FSMContext):
    await state.set_state(ConvertStates.convert_for_images)
    lang = message.from_user.language_code if message.from_user else None
    await message.answer(
        get_texts(lang).SEND_IMAGE,
        reply_markup=get_back_keyboard(lang)
    )


@router.message(StateFilter(ConvertStates.main_menu), F.text.contains("🗒"))
@router.message(Command("txt"))
async def set_txt_mode(message: types.Message, state: FSMContext):
    await state.set_state(ConvertStates.convert_for_txt)
    lang = message.from_user.language_code if message.from_user else None
    await message.answer(
        get_texts(lang).SEND_TXT,
        reply_markup=get_back_keyboard(lang)
    )


# ---------------------------
# STATE NONE
# ---------------------------
@router.message(StateFilter(None))
async def handle_none_state(message: types.Message, state: FSMContext):
    await state.set_state(ConvertStates.main_menu)
    lang = message.from_user.language_code if message.from_user else None
    texts = get_texts(lang)

    # We visually show that the interface has been updated
    temp_msg = await message.answer(texts.UPDATE_SYSTEM, reply_markup=ReplyKeyboardRemove())
    await asyncio.sleep(1)
    await temp_msg.delete()

    await message.answer(
        texts.STATE_NONE,
        reply_markup=get_menu_keyboard(lang)
    )


# ---------------------------
# FALLBACK
# ---------------------------
@router.message(StateFilter(ConvertStates.main_menu))
async def main_menu_fallback(message: types.Message):
    await send_unsupported_content(message)
