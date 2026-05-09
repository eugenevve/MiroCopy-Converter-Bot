from aiogram import types
from aiogram.fsm.context import FSMContext
from bot.keyboards.menu import get_menu_keyboard
from bot.locales.index import get_texts
from bot.utils.states import ConvertStates


async def return_to_main_menu(message: types.Message, state: FSMContext):
    await state.set_state(ConvertStates.main_menu)
    lang = message.from_user.language_code if message.from_user else None
    await message.answer(
        get_texts(lang).START,
        reply_markup=get_menu_keyboard(lang)
    )
