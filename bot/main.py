import asyncio
import logging
import sys

from config import TOKEN

from aiogram import Bot, Dispatcher
from handlers import callbacks, commands, message


async def main():
  bot = Bot(token=TOKEN)
  dp = Dispatcher()
  dp.include_router(callbacks.router)
  dp.include_router(commands.router)
  dp.include_router(message.router)
  await dp.start_polling(bot)

if __name__ == "__main__":
  logging.basicConfig(level=logging.INFO, stream=sys.stdout)
  try:
    asyncio.run(main())
  except KeyboardInterrupt:
    print('Exit')