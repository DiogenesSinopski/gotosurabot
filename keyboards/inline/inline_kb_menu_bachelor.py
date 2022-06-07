from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_menu_bachelor = InlineKeyboardMarkup(row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Фінанси …', callback_data='Фінанси'),
            InlineKeyboardButton(text='Діджитал маркетинг', callback_data='Маркетинг')
        ],
        [
            InlineKeyboardButton(text='Діджитал облік і консалтинг', callback_data='Облік'),
            InlineKeyboardButton(text='Цифрова економіка', callback_data='Економіка')
        ],
        [
            InlineKeyboardButton(text='Соціокультурна …', callback_data='Соціокультурна'),
            InlineKeyboardButton(text='Готельна справа …', callback_data='Готельна')
        ],
        [
            InlineKeyboardButton(text='Філологія Переклад', callback_data='Філологія'),
            InlineKeyboardButton(text='Туризм', callback_data='Туризм')
        ],
        [
            InlineKeyboardButton(text='Правоохоронна …', callback_data='Правоохоронна'),
            InlineKeyboardButton(text='Право', callback_data='Право')
        ],
        [
            InlineKeyboardButton(text='Аналітика даних …', callback_data='Аналітика'),
            InlineKeyboardButton(text='Адміністрування …', callback_data='Адміністрування')
        ],
        [
            InlineKeyboardButton(text='Інформаційне забезпечення', callback_data='Інформаційне'),
            InlineKeyboardButton(text='Графічний дизайн', callback_data='Дизайн')
        ]
    ]
)