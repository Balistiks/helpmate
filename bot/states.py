from aiogram.filters.state import State, StatesGroup

class RegisterCustumer(StatesGroup):
  fio = State()
  phone_number = State()
  mail = State()
  adress = State()
  