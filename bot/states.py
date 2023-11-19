from aiogram.filters.state import State, StatesGroup

class ChangeCustumer(StatesGroup):
  fio = State()
  phone_number = State()

  