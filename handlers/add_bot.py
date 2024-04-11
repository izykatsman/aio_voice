from aiogram import Router, Bot
from aiogram.types import ChatMemberUpdated, FSInputFile
from aiogram.filters.chat_member_updated import ChatMemberUpdatedFilter, JOIN_TRANSITION

from db.db import get_hellow, get_chat, set_new_chat

router = Router()


@router.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=JOIN_TRANSITION))
async def bot_added_as_member(event: ChatMemberUpdated, bot: Bot):
    hellow = get_hellow()

    if get_chat(event.chat.id) is None:
        set_new_chat(event.chat.id, event.chat.username)

    if hellow['image'] is None:
        if hellow['text'] is not None:
            await bot.send_message(event.chat.id, hellow['text'])
    else:
        if hellow['text'] is not None:
            await bot.send_photo(event.chat.id, photo=FSInputFile(f"{hellow['image']}"), caption=hellow['text'])
        else:
            await bot.send_photo(event.chat.id, photo=FSInputFile(f"{hellow['image']}"))
