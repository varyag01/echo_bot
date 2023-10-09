import asyncio

from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers import othe_handlers, user_handlers

async def main() -> None:

    config: Config = load_config("D:\программирование\репозитории\My_first_repository\8.3\Telegramm_bot_Shablon\.env")

    bot = Bot (token=config.tg_bot.token)
    dp = Dispatcher()

    dp.include_router (user_handlers.router)
    dp.include_router (othe_handlers.router)

    await bot.delete_webhook (drop_pending_updates=True)
    await dp.start_polling (bot)

if __name__ == "__main__":
    asyncio.run(main())
