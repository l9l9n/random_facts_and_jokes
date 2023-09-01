from aiogram import Bot, Dispatcher, types, executor
from config import TOKEN
import pyjokes
from googletrans import Translator



bot = Bot(TOKEN)
dp = Dispatcher(bot)
translator = Translator()

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton(text='Анекдот')
keyboard.add(btn1)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer('Привет!\nЯ умею отправлять анекдоты!', reply_markup=keyboard)


@dp.message_handler(text='Анекдот')
async def cmd_start(message: types.Message):
    joke = pyjokes.get_joke()
    translation = translator.translate(joke, dest='ru')
    await message.answer(translation.text)


if __name__ == '__main__':
    executor.start_polling(dp)