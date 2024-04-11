from aiogram import Router, Bot
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile
from pyrogram import Client

from config import admin_id
from filters.admin_filter import AdminsFilter

router = Router()


@router.message(Command("add"), AdminsFilter())
async def start(message: Message, pyro_bot: Client):
    splitted = message.text.split(' ')
    if len(splitted) == 2:
        await pyro_bot.promote_chat_member(int(splitted[1]), admin_id)
    else:
        await message.answer(f"Вы ввели не верное количество аргументов {len(splitted)}, а ожидалось 2.")


@router.message(Command('parse'), AdminsFilter())
async def parse_handle(message: Message, pyro_bot: Client, bot: Bot):
    splitted = message.text.split(' ')
    if len(splitted) == 2:
        with open(f'chat_{splitted[1]}.txt', 'a') as file:
            async for member in pyro_bot.get_chat_members(int(splitted[1])):
                file.write(f'@{member.user.username}\n')
            document = FSInputFile(f'chat_{splitted[1]}.txt')
            await message.answer_document(document)
    else:
        await message.answer(f"Вы ввели не верное количество аргументов {len(splitted)}, а ожидалось 2.")
