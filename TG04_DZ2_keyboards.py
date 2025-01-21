from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

inline_keyboard_test = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text="Новости", url="http://ria.ru/20250121/trump-1994799834.html")],
   [InlineKeyboardButton(text="Музыка", url="http://rutube.ru/feeds/music/musicgenres/")],
   [InlineKeyboardButton(text="Видео", url="http://rutube.ru/video/d8d4c6653d448704bd221673fa65f173")]
])

# Задание 2: Кнопки с URL-ссылками
# При отправке команды /links бот будет показывать инлайн-кнопки с URL-ссылками.
# Создайте три кнопки с ссылками на новости/музыку/видео