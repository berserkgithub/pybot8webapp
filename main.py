from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo


bot = Bot('5833123557:AAEKwKlMcR-6MbAeqdYdVsgufixnMBGCSnc')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть веб страницу', web_app=WebappInfo(url='https://google.com')))
    await message.answer('Привет, мой друг', reply_markup=markup)