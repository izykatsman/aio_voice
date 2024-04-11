from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile

from db.db import get_hellow, get_user, set_new_user
from filters.admin_filter import AdminsFilter

from keyboards.inline import start_admin_keyboard

router = Router()


@router.message(Command("start"), ~AdminsFilter())
async def start(message: Message):
    hellow = get_hellow()
    # TODO проверять, что это лс

    if get_user(message.chat.id) is None:
        set_new_user(message.chat.id, message.chat.username)

    if hellow['image'] is None:
        if hellow['text'] is not None:
            await message.answer(hellow['text'], reply_markup=start_admin_keyboard())
    else:
        if hellow['text'] is not None:
            await message.answer_photo(photo=FSInputFile(f"{hellow['image']}"), caption=hellow['text'],
                                       reply_markup=start_admin_keyboard())
        else:
            await message.answer_photo(photo=FSInputFile(f"{hellow['image']}"), reply_markup=start_admin_keyboard())


@router.message(Command("start"), AdminsFilter())
async def start(message: Message):
    hellow = get_hellow()

    if hellow['image'] is None:
        if hellow['text'] is not None:
            await message.answer(hellow['text'], reply_markup=start_admin_keyboard())
    else:
        if hellow['text'] is not None:
            await message.answer_photo(photo=FSInputFile(f"{hellow['image']}"), caption=hellow['text'],
                                       reply_markup=start_admin_keyboard())
        else:
            await message.answer_photo(photo=FSInputFile(f"{hellow['image']}"), reply_markup=start_admin_keyboard())
