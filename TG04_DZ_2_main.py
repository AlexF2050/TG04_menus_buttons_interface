# Задание 2: Кнопки с URL-ссылками
# При отправке команды /links бот будет показывать инлайн-кнопки с URL-ссылками.
# Создайте три кнопки с ссылками на новости/музыку/видео

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
    await message.answer("Привет!")

@dp.message(Command('links'))
async def links(message: Message):
    await message.answer('Вот свежие новости!', reply_markup=kb.inline_keyboard_test)

async def main():                                  # цикл обработки сообщений
    await dp.start_polling(bot)                    # запуск обработки сообщений

if __name__ == '__main__':
    asyncio.run(main())