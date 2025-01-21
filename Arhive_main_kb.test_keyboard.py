import asyncio
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile
import random
from gtts import gTTS
import os
from googletrans import Translator
from config import TOKEN
import keyboards as kb

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Доброго времени, {message.from_user.first_name} напиши мне любой текст, и я переведу его на английский язык.", reply_markup=await kb.test_keyboard())  # , reply_markup=kb.inline_keyboard_test или reply_markup=kb.main

@dp.message(Command('help'))
async def help(message: Message):
    await message.answer("Этот бот умеет выполнять эти команды : \n /start \n /help") # ответ на сообщение

@dp.message(Command('voice'))
async def voice(message: Message):
    voice = FSInputFile('sample.ogg') # голосовое сообщение формата .ogg
    await message.answer_voice(voice) # отправка голосового сообщения

@dp.message(F.photo)
async def react_photo(message: Message):
    list = ['Ого, какая фотка!', 'Непонятно, что это такое', 'Не отправляй мне такое больше']
    rand_answ = random.choice(list)
    await message.answer(rand_answ)
    await bot.download(message.photo[-1],destination=f'tmp/{message.photo[-1].file_id}.jpg') # сохраняем фото в папку tmp

# Инициализация переводчика
translator = Translator()

@dp.message(Command('tr'))
async def send_welcome(message: types.Message):
    await message.reply("Привет! Напиши мне любой текст, и я переведу его на английский язык.")

@dp.message()
async def translate_message(message: types.Message):
    # Перевод входящего сообщения на английский
    translated = await translator.translate(message.text, dest='en')
    await message.reply(translated.text)

async def main():                                  # цикл обработки сообщений
    await dp.start_polling(bot)                    # запуск обработки сообщений

if __name__ == '__main__':
    asyncio.run(main())