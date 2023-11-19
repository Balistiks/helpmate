from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from db.model import async_session

import db.requests as request
import keyboards as kb

from states import ChangeCustumer

import logging

logger = logging.getLogger(__name__)

router = Router()

@router.message(ChangeCustumer.fio)
async def change_fio(message: Message, state: FSMContext):
  # Изменение user
  await request.update(message.from_user.id, message.text, 'fio')

  await state.clear()
  await message.answer('Данные успешно актуализированы', reply_markup=kb.to_main_menu)

@router.message(ChangeCustumer.phone_number)
async def change_phone_number(message: Message, state: FSMContext):
  # Изменение user
  await request.update(message.from_user.id, message.text, 'phone')
  
  await state.clear()
  await message.answer('Данные успешно актуализированы', reply_markup=kb.to_main_menu)
  