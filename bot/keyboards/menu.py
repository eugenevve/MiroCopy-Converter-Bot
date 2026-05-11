from aiogram.enums import ButtonStyle
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from bot.locales.index import get_texts


def get_menu_keyboard(lang: str | None) -> ReplyKeyboardMarkup:
    texts = get_texts(lang)
    keyboard = [
        [KeyboardButton(
            text=texts.BTN_IMAGE_TO_PDF,
            style=ButtonStyle.SUCCESS
        )],
        [KeyboardButton(
            text=texts.BTN_TXT_TO_PDF,
            style=ButtonStyle.SUCCESS
        )],
    ]
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
    )
