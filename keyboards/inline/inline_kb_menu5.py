from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_menu5 = InlineKeyboardMarkup(row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Фінанси …', callback_data='Фінанси'),
            InlineKeyboardButton(text='Діджитал маркетинг', callback_data='Діджитал маркетинг')
        ],
        [
            InlineKeyboardButton(text='Діджитал облік', callback_data='Діджитал облік'),
            InlineKeyboardButton(text='Цифрова економіка', callback_data='Цифрова економіка')
        ],
        [
            InlineKeyboardButton(text='Соціокультурна …', callback_data='Менеджмент та адміністрування'),
            InlineKeyboardButton(text='Готельна справа …', callback_data='готельно')
        ],
        [
            InlineKeyboardButton(text='Філологія Переклад', callback_data='Германська'),
            InlineKeyboardButton(text='Туризм', callback_data='Туризм')
        ],
        [
            InlineKeyboardButton(text='Правоохоронна …', callback_data='Правоохоронна діяльність'),
            InlineKeyboardButton(text='Право', callback_data='Право')
        ],
        [
            InlineKeyboardButton(text='Аналітика даних …', callback_data='Інформаційна'),
            InlineKeyboardButton(text='Адміністрування …', callback_data='Бізнес')
        ],
        [
            InlineKeyboardButton(text='Інформаційне забезпечення', callback_data='Документаційно-інформаційне')
        ]
    ]
)
