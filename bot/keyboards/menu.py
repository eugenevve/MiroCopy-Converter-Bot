from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from bot.locales.index import get_texts


def get_menu_keyboard(lang: str | None) -> ReplyKeyboardMarkup:
    texts = get_texts(lang)
    keyboard = [
        [KeyboardButton(text=texts.BTN_PHOTO_TO_PDF)],
    ]
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
    )
