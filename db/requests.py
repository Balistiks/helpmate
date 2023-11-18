from sqlalchemy import select

from db.model import User, async_session

async def get_user_by_tg_id(tg_id):
  async with async_session() as session:
    result = await session.scalars(select(User).where(User.tg_id == tg_id))
    return result
