# Кнопки клавиатуры

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
   [KeyboardButton(text="Кнопка 1")],
   [KeyboardButton(text="Кнопка 2"), KeyboardButton(text="Кнопка 3")]
], resize_keyboard=True)

inline_keyboard_test = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text="Каталог", callback_data='catalog')],
   [InlineKeyboardButton(text="Новости", callback_data='news')],
   [InlineKeyboardButton(text="Профиль", callback_data='person')],
#   [InlineKeyboardButton(text="Ссылка", url="http://rutube.ru/video/d8d4c6653d448704bd221673fa65f173")]
])

test = ["кнопка 1", "кнопка 2", "кнопка 3", "кнопка 4"]
async def test_keyboard():
   keyboard = InlineKeyboardBuilder()
   for key in test:
       keyboard.add(InlineKeyboardButton(text=key, url='http://rutube.ru/video/d8d4c6653d448704bd221673fa65f173'))
   return keyboard.adjust(2).as_markup()