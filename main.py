import asyncio

from aiogram import Bot, Dispatcher
from pyrogram import Client

from config import main_bot

from handlers import start, add_bot, service, admin

import logging

from middleware.ai_midleware import AIMiddleware
from speech2text.ai import train_model

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.WARNING,
    format="%(asctime)s|%(levelname)s|%(name)s|%(message)s",
    datefmt='%Y-%m-%d|%H:%M:%S'
)


async def main() -> None:
    pipe = train_model()
    bot = Bot(main_bot)
    pyro_bot = Client('pyro_bot', api_id=9316057, api_hash='455f1f968ab9be80b532470163aabdbe', bot_token=main_bot)
    await pyro_bot.start()

    dp = Dispatcher(pyro_bot=pyro_bot)
    dp.include_router(start.router)
    dp.include_router(add_bot.router)
    dp.include_router(service.router)
    dp.include_router(admin.router)

    dp.message.outer_middleware(AIMiddleware(pipe))
    logger.warning("Starting aiogram polling")

    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    asyncio.run(main())
