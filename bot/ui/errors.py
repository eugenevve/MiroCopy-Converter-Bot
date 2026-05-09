from aiogram import types
from bot.locales.index import get_texts


async def send_unsupported_content(message: types.Message):
    lang = message.from_user.language_code if message.from_user else None
    await message.answer(
        get_texts(lang).UNSUPPORTED_CONTENT
    )
