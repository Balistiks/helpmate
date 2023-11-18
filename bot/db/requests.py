from sqlalchemy import select

from db.model import User, async_session

async def user_exist(tg_id):
  async with async_session() as session:
    # Проверка существования кода
    result = await session.execute(select(User).where(User.tg_id == tg_id))
    user = result.first()
    return user
