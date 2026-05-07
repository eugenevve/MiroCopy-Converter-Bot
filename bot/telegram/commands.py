from aiogram import Bot
from aiogram.types import BotCommand

from bot.locales.index import get_texts
from bot.utils.enums import Command, Locales


def get_lang_commands(lang_code: str) -> list[BotCommand]:
    texts = get_texts(lang_code)
    return [
        BotCommand(command=Command.START, description=texts.START_CMD),
    ]


async def set_commands(bot: Bot) -> None:
    languages = [
        Locales.RU,
        Locales.ES,
        Locales.PT,
        Locales.ID,
        Locales.AR
    ]

    await bot.set_my_commands(get_lang_commands(Locales.EN))

    for lang in languages:
        await bot.set_my_commands(get_lang_commands(lang), language_code=lang)
