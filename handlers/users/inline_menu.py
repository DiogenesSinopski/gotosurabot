from aiogram import types
from aiogram.types import CallbackQuery, Message, InputFile
from keyboards.inline import ikb_menu_main, ikb_menu_osvitni, ikb_menu_magistracy, ikb_menu_bachelor, ikb_menu_zvyazatysya
from loader import dp

@dp.message_handler(text='Головне меню')
async def show_inline_menu(message: types.Message):
    await message.answer('''Що вміє цей бот?
Бот Фахового коледжу СУРА (м. Черкаси) дозволяє:
- Зв’язатися з нашим консультантом;
- Дізнатися про спеціальності та освітні програми;
- Подати заявку на вступ;
- Запросити про допомогу зі вступу, реєстрації on-line кабінету вступника;
- Дізнатися розпорядок роботи приймальної комісії.

Оберіть що вас цікавить''', reply_markup=ikb_menu_main)

@dp.message_handler(text='Як до нас дібратися')
async def menu_index(message: types.Message):
    await message.answer_location(latitude=49.40548059551326, longitude=32.05391222883521)

@dp.callback_query_handler(text='Освітні програми')
async def send_message(call: CallbackQuery):
    await call.message.edit_reply_markup(ikb_menu_osvitni)

@dp.callback_query_handler(text='Вступнику')
async def send_message(call: CallbackQuery):
    await call.message.answer('''Розпорядок роботи приймальної комісії
понеділок – п’ятниця з 10.00 до 14.00''')

@dp.callback_query_handler(text='Контакти')
async def send_message(call: CallbackQuery):
    await call.message.answer('''
вул. Нечуя-Левицького, 16
м. Черкаси, 18028, Україна
Телефон: (0472) 64-70-55
Телефон приймальної комісії:
(099) 105-27-71, (098) 340-10-36,
(063) 799-42-51
Університет: rauniver@suem.edu.ua
Коледж: college@suem.edu.ua
    ''')

@dp.callback_query_handler(text='Магістр')
async def send_message(call: CallbackQuery):
    await call.message.edit_reply_markup(ikb_menu_magistracy)

@dp.callback_query_handler(text='Зв’язатися')
async def send_message(call: CallbackQuery):
    await call.message.edit_reply_markup(ikb_menu_zvyazatysya)

@dp.callback_query_handler(text='Бакалавр')
async def send_message(call: CallbackQuery):
    await call.message.edit_reply_markup(ikb_menu_bachelor)

@dp.callback_query_handler(text='Подзвонити')
async def menu_index(call: types.CallbackQuery):
    await call.message.answer_contact(phone_number='+380991052771', first_name='СУЕМ')



@dp.callback_query_handler(text='Маркетинг')
async def menu_index(call: types.CallbackQuery):
    await call.message.answer_photo(photo=InputFile(path_or_bytesio='media/Digitsl_mark.jpg'))

@dp.callback_query_handler(text='Правоохоронна')
async def menu_index(call: types.CallbackQuery):
    await call.message.answer_photo(photo=InputFile(path_or_bytesio='media/Pravo_dizl.jpg'))

@dp.callback_query_handler(text='Соціокультурна')
async def menu_index(call: types.CallbackQuery):
    await call.message.answer_photo(photo=InputFile(path_or_bytesio='media/Menedzh_.jpg'))

@dp.callback_query_handler(text='Облік')
async def menu_index(call: types.CallbackQuery):
    await call.message.answer_photo(photo=InputFile(path_or_bytesio='media/Obl_.jpg'))

@dp.callback_query_handler(text='Фінанси')
async def menu_index(call: types.CallbackQuery):
    await call.message.answer_photo(photo=InputFile(path_or_bytesio='media/Fin.jpg'))

@dp.callback_query_handler(text='Адміністрування')
async def menu_index(call: types.CallbackQuery):
    await call.message.answer_photo(photo=InputFile(path_or_bytesio='media/Biznes_adm.jpg'))

@dp.callback_query_handler(text='Економіка')
async def menu_index(call: types.CallbackQuery):
    await call.message.answer_photo(photo=InputFile(path_or_bytesio='media/Cifra_econom.jpg'))

@dp.callback_query_handler(text='Право')
async def menu_index(call: types.CallbackQuery):
    await call.message.answer_photo(photo=InputFile(path_or_bytesio='media/Pravo.jpg'))

@dp.callback_query_handler(text='Філологія')
async def menu_index(call: types.CallbackQuery):
    await call.message.answer_photo(photo=InputFile(path_or_bytesio='media/Pereklad.jpg'))

@dp.callback_query_handler(text='Туризм')
async def menu_index(call: types.CallbackQuery):
    await call.message.answer_photo(photo=InputFile(path_or_bytesio='media/Turizm.jpg'))

@dp.callback_query_handler(text='Готельна')
async def menu_index(call: types.CallbackQuery):
    await call.message.answer_photo(photo=InputFile(path_or_bytesio='media/GRS.jpg'))

@dp.callback_query_handler(text='Інформаційне')
async def menu_index(call: types.CallbackQuery):
    await call.message.answer_photo(photo=InputFile(path_or_bytesio='media/Docum.jpg'))

@dp.callback_query_handler(text='Аналітика')
async def menu_index(call: types.CallbackQuery):
    await call.message.answer_photo(photo=InputFile(path_or_bytesio='media/Inf.jpg'))

@dp.callback_query_handler(text='Дизайн')
async def menu_index(call: types.CallbackQuery):
    await call.message.answer_photo(photo=InputFile(path_or_bytesio='media/'))



@dp.callback_query_handler(text='Фінанси_mag')
async def menu_index(call: types.CallbackQuery):
    await call.message.answer_photo(photo=InputFile(path_or_bytesio='media/Fin_mag.jpg'))

@dp.callback_query_handler(text='Маркетинг_mag')
async def menu_index(call: types.CallbackQuery):
    await call.message.answer_photo(photo=InputFile(path_or_bytesio='media/Digitsl_mark_mag.jpg'))

@dp.callback_query_handler(text='Облік_mag')
async def menu_index(call: types.CallbackQuery):
    await call.message.answer_photo(photo=InputFile(path_or_bytesio='media/Obl_mag.jpg'))

@dp.callback_query_handler(text='Адміністрування_mag')
async def menu_index(call: types.CallbackQuery):
    await call.message.answer_photo(photo=InputFile(path_or_bytesio='media/Biznes_adm_mag.jpg'))

@dp.callback_query_handler(text='Економіка_mag')
async def menu_index(call: types.CallbackQuery):
    await call.message.answer_photo(photo=InputFile(path_or_bytesio='media/Cifra_econom_mag.jpg'))

@dp.callback_query_handler(text='Право_mag')
async def menu_index(call: types.CallbackQuery):
    await call.message.answer_photo(photo=InputFile(path_or_bytesio='media/Pravo_mag.jpg'))

@dp.callback_query_handler(text='Філологія_mag')
async def menu_index(call: types.CallbackQuery):
    await call.message.answer_photo(photo=InputFile(path_or_bytesio='media/Pereklad_mag.jpg'))

@dp.callback_query_handler(text='Готельна_mag')
async def menu_index(call: types.CallbackQuery):
    await call.message.answer_photo(photo=InputFile(path_or_bytesio='media/GRS_mag.jpg'))

@dp.callback_query_handler(text='Інформаційне_mag')
async def menu_index(call: types.CallbackQuery):
    await call.message.answer_photo(photo=InputFile(path_or_bytesio='media/Doc_inf_mag.jpg'))






