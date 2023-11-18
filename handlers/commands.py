from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
import keyboards as kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
  await message.answer('Привет, кто ты?', reply_markup=kb.main)