from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
   [KeyboardButton(text="Привет")],
   [KeyboardButton(text="Пока")]
], resize_keyboard=True)

# Задание 1: Создание простого меню с кнопкам и
# При отправке команды /start бот будет показывать меню с кнопками "Привет" и "Пока".
# При нажатии на кнопку "Привет" бот должен отвечать "Привет, {имя пользователя}!",
# а при нажатии на кнопку "Пока" бот должен отвечать "До свидания, {имя пользователя}!".