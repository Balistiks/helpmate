from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types.web_app_info import WebAppInfo

main = InlineKeyboardMarkup(inline_keyboard=[
  [InlineKeyboardButton(text='Заказчик', callback_data='customer')],
  [InlineKeyboardButton(text='Испольнитель', callback_data='executor')]
], resize_keyboard=True)

register = InlineKeyboardMarkup(inline_keyboard=[
  [InlineKeyboardButton(text='Зарегестрироваться', web_app=WebAppInfo(url='https://localhost:3000/register'))]
])





