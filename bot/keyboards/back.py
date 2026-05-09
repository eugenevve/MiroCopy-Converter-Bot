from aiogram.enums import ButtonStyle
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from bot.locales.index import get_texts


def get_back_keyboard(lang: str | None) -> ReplyKeyboardMarkup:
    texts = get_texts(lang)
    keyboard = [
        [KeyboardButton(
            text=texts.BTN_BACK,
            style=ButtonStyle.PRIMARY
        )],
    ]
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
    )
