import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from systems.client import router as client_router
from utils.config_connection import API_TOKEN
from utils.logger import logger

# Инициализация токена бота
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Команды для контекстного меню
async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="🔄 Restart"),
    ]
    await bot.set_my_commands(commands)

# Инициализация систем
dp.include_router(client_router)

# Запускаемая функция бота
async def main():
    await set_commands(bot)
    logger.info("🔄 Бот запускается...")
    try:
        await dp.start_polling(bot)
    except Exception as e:
        logger.exception(f"❌ Ошибка при старте polling: {e}")

# Запуск системы бота
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("🛑 Бот остановлен пользователем")
