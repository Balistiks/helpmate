from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types.web_app_info import WebAppInfo

main = InlineKeyboardMarkup(inline_keyboard=[
  [InlineKeyboardButton(text='Заказчик', callback_data='customer')],
  [InlineKeyboardButton(text='Испольнитель', callback_data='executor')]
], resize_keyboard=True)

register = InlineKeyboardMarkup(inline_keyboard=[
  [InlineKeyboardButton(text='Зарегестрироваться', web_app=WebAppInfo(url='https://help-mate.ru/register'))]
], resize_keyboard=True)

menu = InlineKeyboardMarkup(inline_keyboard=[
  [InlineKeyboardButton(text='Оставить заявку', web_app=WebAppInfo(url='https://help-mate.ru/register'))],
  [InlineKeyboardButton(text='Личный кабинет', callback_data='lk')]
], resize_keyboard=True)

lk_menu = InlineKeyboardMarkup(inline_keyboard=[
  [InlineKeyboardButton(text='Изменить данные', callback_data='change_data_lk')],
  [InlineKeyboardButton(text='В главное меню', callback_data='customer')]
], resize_keyboard=True)


columns_for_change_lk = InlineKeyboardMarkup(inline_keyboard=[
  [InlineKeyboardButton(text='ФИО', callback_data='change_lk_fio')],
  [InlineKeyboardButton(text='Номер телефона', callback_data='change_lk_phone_number')]
], resize_keyboard=True)

to_main_menu = InlineKeyboardMarkup(inline_keyboard=[
  [InlineKeyboardButton(text='В главное меню', callback_data='customer')]
], resize_keyboard=True)