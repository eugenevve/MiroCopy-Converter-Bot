from aiogram.types import BotCommand

from bot.telegram.enums import Command


def get_commands_en():
    return [
        BotCommand(command=Command.START, description="🔄 Restart bot"),
    ]


def get_commands_ru():
    return [
        BotCommand(command=Command.START, description="🔄 Перезапустить бота"),
    ]


def get_commands_es():
    return [
        BotCommand(command=Command.START, description="🔄 Reiniciar el bot"),
    ]


def get_commands_pt():
    return [
        BotCommand(command=Command.START, description="🔄 Reiniciar o bot"),
    ]


def get_commands_id():
    return [
        BotCommand(command=Command.START, description="🔄 Mulai ulang bot"),
    ]


def get_commands_ar():
    return [
        BotCommand(command=Command.START, description="🔄 إعادة تشغيل البوت"),
    ]
