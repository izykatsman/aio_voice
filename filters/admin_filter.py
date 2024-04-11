from aiogram.filters import BaseFilter
from aiogram.types import Message, CallbackQuery

from config import admin_id


class AdminsFilter(BaseFilter):
    async def __call__(self, event: [Message, CallbackQuery]) -> bool:
        if event.from_user.id == admin_id:
            return True

        return False
