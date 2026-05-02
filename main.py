import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.client.default import DefaultBotProperties

from bot.core.config import API_TOKEN
from bot.handlers.convert import router as client_router
from bot.core.logger import logger
from bot.telegram.commands import (
    get_commands_en,
    get_commands_ru,
    get_commands_es,
    get_commands_pt,
    get_commands_id,
    get_commands_ar,
)


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)


async def set_commands(bot: Bot) -> None:
    # default
    await bot.set_my_commands(get_commands_en())

    # localized
    await bot.set_my_commands(get_commands_en(), language_code="en")
    await bot.set_my_commands(get_commands_ru(), language_code="ru")
    await bot.set_my_commands(get_commands_es(), language_code="es")
    await bot.set_my_commands(get_commands_pt(), language_code="pt")
    await bot.set_my_commands(get_commands_id(), language_code="id")
    await bot.set_my_commands(get_commands_ar(), language_code="ar")


async def main() -> None:
    logger.info("🔄 Bot is starting...")

    bot = Bot(
        token=API_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )

    dp = Dispatcher()
    dp.include_router(client_router)

    await set_commands(bot)

    try:
        await dp.start_polling(bot)
    except Exception:
        logger.exception("❌ Error while starting polling")
    finally:
        await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("🛑 Bot stopped by user")
