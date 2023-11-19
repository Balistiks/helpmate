from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from states import ChangeCustumer

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
  """, reply_markup=kb.lk_menu)
  await callback.answer()

@router.callback_query(F.data == 'change_data_lk')
async def change_lk_menu(callback: CallbackQuery):
  # получение пользователя по tg_id
  user = await request.get_user_by_tg_id(callback.from_user.id)
  # Выведение ифнормации о пользователе
  await callback.message.edit_text(f"""
ФИО: {user.fio}
Номер телефона: {user.phone_numebr}

Выберите что хотите изменить
""", reply_markup=kb.columns_for_change_lk)
  await callback.answer()

@router.callback_query(F.data.startswith('change_lk_'))
async def change_lk(callback: CallbackQuery, state: FSMContext):
  # Проверка какой столбец мы меняем
  if (callback.data == 'change_lk_fio'):
    await callback.message.edit_text('Напишите свое ФИО:', reply_markup=None)
    await state.set_state(ChangeCustumer.fio)
  elif (callback.data == 'change_lk_phone_number'):
    await callback.message.edit_text('Напишите свой номер телефона:', reply_markup=None)
    await state.set_state(ChangeCustumer.phone_number)
  await callback.answer()