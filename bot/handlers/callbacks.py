from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

import db.requests as request
import keyboards as kb

router = Router()

@router.callback_query(F.data == 'customer')
async def customer(callback: CallbackQuery):
  # есть ли такой пользователь
  user = await request.user_exist(callback.from_user.id)
  if (user):
    await callback.message.edit_text('Меню', reply_markup=kb.menu)
  else:
    await callback.message.answer('Для использования нашего приложения, вам нужно пройти регистрацию как заказчик', reply_markup=kb.register)
  await callback.answer()

@router.callback_query(F.data == 'lk')
async def personal_area(callback: CallbackQuery):
  # получение пользователя по tg_id
  user = await request.get_user_by_tg_id(callback.from_user.id)
  # Выведение ифнормации о пользователе
  await callback.message.edit_text(f"""
ФИО: {user.fio}
Номер телефона: {user.phone_numebr}
Адрес: {user.adress}
  """)
  await callback.answer()