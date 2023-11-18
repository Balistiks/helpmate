from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

main = InlineKeyboardMarkup(inline_keyboard=[
  [InlineKeyboardButton(text='Заказчик', callback_data='customer')],
  [InlineKeyboardButton(text='Испольнитель', callback_data='executor')]
], resize_keyboard=True)





