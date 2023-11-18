from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

import db.requests as request

router = Router()

@router.callback_query(F.data == 'customer')
async def customer(callback: CallbackQuery):
  user = await request.get_user_by_tg_id(callback.from_user.id)
  print(user)
  await callback.message.answer('Custumer')