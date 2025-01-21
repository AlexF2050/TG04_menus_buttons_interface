from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

inline_keyboard_test = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text="Показать больше", callback_data='dynamic')]
])

test = ["опция 1", "опция 2"]
urls = {
    "опция 1": "http://rutube.ru/feeds/top/",
    "опция 2": "http://rutube.ru/feeds/live/"
}
async def test_keyboard():
   keyboard = InlineKeyboardBuilder()
   for key in test:
       keyboard.add(InlineKeyboardButton(text=key, url=urls[key]))
   return keyboard.adjust(2).as_markup()

# Задание 3: Динамическое изменение клавиатуры
# При отправке команды /dynamic бот будет показывать инлайн-кнопку "Показать больше".
# При нажатии на эту кнопку бот должен заменять её на две новые кнопки "Опция 1" и "Опция 2".
# При нажатии на любую из этих кнопок бот должен отправлять сообщение с текстом выбранной опции.