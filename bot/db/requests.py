from sqlalchemy import select

from db.model import User, async_session

async def user_exist(tg_id):
  async with async_session() as session:
    # Проверка существования кода
    result = await session.execute(select(User).where(User.tg_id == tg_id))
    user = result.first()
    return user
  
async def get_user_by_tg_id(tg_id):
  async with async_session() as session:
    print(f'jsdngbiundfighndfjhuogj {tg_id}')
    # получение данных
    result = await session.execute(select(User).where(User.tg_id == tg_id))
    user = result.scalar()
    return user

async def update(tg_id, text, column):
  async with async_session() as session:
    # получение данных
    result = await session.execute(select(User).where(User.tg_id == tg_id))
    user = result.scalar()
    if (column == 'fio'):
      user.fio = text
    elif (column == 'phone'):
      user.phone_numebr = text
    await session.commit()