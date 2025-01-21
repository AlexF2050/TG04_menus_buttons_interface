# Задание 1: Создание простого меню с кнопкам и
# При отправке команды /start бот будет показывать меню с кнопками "Привет" и "Пока".
# При нажатии на кнопку "Привет" бот должен отвечать "Привет, {имя пользователя}!",
# а при нажатии на кнопку "Пока" бот должен отвечать "До свидания, {имя пользователя}!".

import asyncio
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile, CallbackQuery
from config import TOKEN
import keyboards as kb

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Выберите действие:", reply_markup=kb.main)

@dp.message(lambda message: message.text == "Привет")
async def hello(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}!")

@dp.message(lambda message: message.text == "Пока")
async def goodbye(message: Message):
    await message.answer(f"До свидания, {message.from_user.first_name}!")

async def main():                                  # цикл обработки сообщений
    await dp.start_polling(bot)                    # запуск обработки сообщений

if __name__ == '__main__':
    asyncio.run(main())