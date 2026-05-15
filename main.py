import asyncio

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.client.default import DefaultBotProperties

from bot.core.config import API_TOKEN, DEBUG_MODE
from bot.handlers import get_handlers_router
from bot.core.logging import logger
from bot.telegram.commands import set_commands
from bot.telegram.description import set_description


async def main() -> None:
    logger.info("🔄 Bot is starting...")

    bot = Bot(
        token=API_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )

    dp = Dispatcher()
    dp.include_router(get_handlers_router())

    if not DEBUG_MODE:
        await set_commands(bot)
        await set_description(bot)

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
