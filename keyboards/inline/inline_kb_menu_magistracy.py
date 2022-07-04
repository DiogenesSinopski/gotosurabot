from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_menu_magistracy = InlineKeyboardMarkup(row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Фінанси …', callback_data='Фінанси_mag'),
            InlineKeyboardButton(text='Діджитал маркетинг', callback_data='Маркетинг_mag')
        ],
        [
            InlineKeyboardButton(text='Облік і оподаткування', callback_data='Облік_mag'),
            InlineKeyboardButton(text='Цифрова економіка', callback_data='Економіка_mag')
        ],
        [
            InlineKeyboardButton(text='Філологія Переклад', callback_data='Філологія_mag'),
            InlineKeyboardButton(text='Готельна справа …', callback_data='Готельна_mag')
        ],
        [
            InlineKeyboardButton(text='Адміністрування …', callback_data='Адміністрування_mag'),
            InlineKeyboardButton(text='Право', callback_data='Право_mag')
        ],
        [
            InlineKeyboardButton(text='Інформаційне забезпечення', callback_data='Інформаційне_mag')
        ]
    ]
)
