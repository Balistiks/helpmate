from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types.web_app_info import WebAppInfo

main = InlineKeyboardMarkup(inline_keyboard=[
  [InlineKeyboardButton(text='Заказчик', callback_data='customer')],
  [InlineKeyboardButton(text='Испольнитель', callback_data='executor')]
], resize_keyboard=True)

register = InlineKeyboardMarkup(inline_keyboard=[
  [InlineKeyboardButton(text='Зарегестрироваться', web_app=WebAppInfo(url='https://youtube.com'))]
], resize_keyboard=True)

menu = InlineKeyboardMarkup(inline_keyboard=[
  [InlineKeyboardButton(text='Оставить заявку', web_app=WebAppInfo(url='https://youtube.com'))],
  [InlineKeyboardButton(text='Личный кабинет', callback_data='lk')]
], resize_keyboard=True)

