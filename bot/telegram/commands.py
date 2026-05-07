from aiogram.types import BotCommand

from bot.locales.index import get_texts
from bot.utils.enums import Command


def get_commands_en():
    return [
        BotCommand(command=Command.START, description=get_texts("en").START_CMD),
    ]


def get_commands_ru():
    return [
        BotCommand(command=Command.START, description=get_texts("ru").START_CMD),
    ]


def get_commands_es():
    return [
        BotCommand(command=Command.START, description=get_texts("es").START_CMD),
    ]


def get_commands_pt():
    return [
        BotCommand(command=Command.START, description=get_texts("pt").START_CMD),
    ]


def get_commands_id():
    return [
        BotCommand(command=Command.START, description=get_texts("id").START_CMD),
    ]


def get_commands_ar():
    return [
        BotCommand(command=Command.START, description=get_texts("ar").START_CMD),
    ]
