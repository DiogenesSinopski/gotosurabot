from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_menu4 = InlineKeyboardMarkup(row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Фінанси …', callback_data='Фінанси1'),
            InlineKeyboardButton(text='Діджитал маркетинг', callback_data='Діджитал маркетинг1')
        ],
        [
            InlineKeyboardButton(text='Діджитал облік', callback_data='Діджитал облік1'),
            InlineKeyboardButton(text='Цифрова економіка', callback_data='Цифрова економіка1')
        ],
        [
            InlineKeyboardButton(text='Філологія Переклад', callback_data='Германська1'),
            InlineKeyboardButton(text='Готельна справа …', callback_data='готельно1')
        ],
        [
            InlineKeyboardButton(text='Адміністрування …', callback_data='Бізнес1'),
            InlineKeyboardButton(text='Право', callback_data='Право1')
        ],
        [
            InlineKeyboardButton(text='Інформаційне забезпечення', callback_data='Документаційно-інформаційне1')
        ]
    ]
)