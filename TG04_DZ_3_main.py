# Задание 3: Динамическое изменение клавиатуры
# При отправке команды /dynamic бот будет показывать инлайн-кнопку "Показать больше".
# При нажатии на эту кнопку бот должен заменять её на две новые кнопки "Опция 1" и "Опция 2".
# При нажатии на любую из этих кнопок бот должен отправлять сообщение с текстом выбранной опции.

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

@dp.message(Command("dynamic"))
async def start(message: Message):
    await message.answer(f"Хороший выбор, {message.from_user.first_name}!", reply_markup=kb.inline_keyboard_test)

@dp.callback_query(F.data == 'dynamic')
async def dynamic(callback: CallbackQuery):
   await callback.message.edit_text('Выберите опцию!', reply_markup=await kb.test_keyboard())

@dp.message(F.text == "опция 1")
async def test_button(message: Message):
   await message.answer('Обработка нажатия на reply кнопку')

async def main():                                  # цикл обработки сообщений
    await dp.start_polling(bot)                    # запуск обработки сообщений

if __name__ == '__main__':
    asyncio.run(main())