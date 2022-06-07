from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_menu_osvitni = InlineKeyboardMarkup(row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Бакалавр', callback_data='Бакалавр'),
            InlineKeyboardButton(text='Магістр', callback_data='Магістр')
        ]
    ]
)