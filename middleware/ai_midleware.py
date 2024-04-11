from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Message

import logging
from logging.handlers import RotatingFileHandler

from transformers import pipeline


# logger = logging.getLogger(__name__)
# logger.propagate = False
# logger.setLevel(logging.DEBUG)
# handler = RotatingFileHandler('logs/middleware.log', maxBytes=1048576, backupCount=3, encoding='utf-8')
# formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
# handler.setFormatter(formatter)
# logger.addHandler(handler)


class AIMiddleware(BaseMiddleware):
    def __init__(self, pipe: pipeline):
        self.pipe = pipe

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        if isinstance(event, Message) and event.voice is not None:
            # TODO взять из базы текст, который надо добавить к расшифровке гс.
            file_id = event.voice.file_id
            file = await data['bot'].get_file(file_id)
            file_path = file.file_path
            await data['bot'].download_file(file_path, "123.ogg")
            text = self.pipe('123.ogg')
            await event.reply(f"{text['text']}\nПриняли гс")
        await handler(event, data)
