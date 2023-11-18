from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
  [KeyboardButton(text='Заказчик')],
  [KeyboardButton(text='Испольнитель')]
], resize_keyboard=True)

