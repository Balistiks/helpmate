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
    pass
  else:
    await callback.message.answer('Для использования нашего приложения, вам нужно пройти регистрацию как заказчик', reply_markup=kb.register)