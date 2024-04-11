from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def start_admin_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Изменить приветствие", callback_data='change_hellow')
            ],
            [
                InlineKeyboardButton(text="Статистика", callback_data='statistic')
            ]
        ]
    )
