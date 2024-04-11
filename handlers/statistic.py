from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery

from db.db import get_all_chats
from filters.admin_filter import AdminsFilter

router = Router()


@router.callback_query(F.data == "statistic", AdminsFilter())
async def callbacks_num_change_fab(callback: CallbackQuery, bot: Bot):
    all_chats = get_all_chats()
    result_text = ''
    all_member_count = 0
    all_active_chats = 0
    for chat in all_chats:
        try:
            member_count = await bot.get_chat_member_count(chat['id'])
            result_text += f'Чат: {chat["id"]}. Количество пользователей: {member_count}'
            all_active_chats += 1
            all_member_count += member_count
        except Exception as e:
            print(e.args)

    if result_text != '':
        await callback.message.answer(result_text)
    else:
        await callback.message.answer(" Чатов еще нет")
