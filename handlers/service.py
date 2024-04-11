from aiogram import Router, F
from aiogram.types import Message

router = Router()


@router.message(F.new_chat_members)
async def somebody_added(message: Message):
    await message.delete()
