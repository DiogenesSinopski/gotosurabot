from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_university = InlineKeyboardMarkup(row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Бакалавр', callback_data='Кнопки5'),
            InlineKeyboardButton(text='Магістр', callback_data='Кнопки4')
        ]
    ]
)