from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command, StateFilter

from bot.keyboards.menu import get_menu_keyboard
from bot.keyboards.back import get_back_keyboard
from bot.locales.index import get_texts
from bot.ui.errors import send_unsupported_content
from bot.utils.states import ConvertStates


router = Router()


# ---------------------------
# START
# ---------------------------
@router.message(Command("start"))
async def cmd_start(message: types.Message, state: FSMContext):
    await state.set_state(ConvertStates.main_menu)
    lang = message.from_user.language_code if message.from_user else None
    await message.answer(
        get_texts(lang).START,
        reply_markup=get_menu_keyboard(lang)
    )


# ---------------------------
# MODES
# ---------------------------
@router.message(StateFilter(ConvertStates.main_menu), F.text.contains("📸"))
async def set_image_mode(message: types.Message, state: FSMContext):
    await state.set_state(ConvertStates.convert_for_images)
    lang = message.from_user.language_code if message.from_user else None
    await message.answer(
        get_texts(lang).SEND_IMAGE,
        reply_markup=get_back_keyboard(lang)
    )


@router.message(StateFilter(ConvertStates.main_menu), F.text.contains("🗒"))
async def set_image_mode(message: types.Message, state: FSMContext):
    await state.set_state(ConvertStates.convert_for_txt)
    lang = message.from_user.language_code if message.from_user else None
    await message.answer(
        get_texts(lang).SEND_TXT,
        reply_markup=get_back_keyboard(lang)
    )


# ---------------------------
# FALLBACK
# ---------------------------
@router.message(StateFilter(ConvertStates.main_menu))
async def main_menu_fallback(message: types.Message):
    await send_unsupported_content(message)
