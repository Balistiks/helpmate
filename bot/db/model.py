from sqlalchemy import BigInteger, String
from sqlalchemy.orm import relationship, Mapped, mapped_column, DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

from config import DATABASE_URL

engine = create_async_engine(DATABASE_URL, echo=True)

async_session = async_sessionmaker(engine)

class Base(AsyncAttrs, DeclarativeBase):
  pass

class User(Base):
  __tablename__ = 'user'

  id: Mapped[int] = mapped_column(primary_key=True)
  tg_id = mapped_column(BigInteger)
  fio = mapped_column(String)
  phone_numebr = mapped_column(String)
  adress = mapped_column(String)

async def async_main():
  async with engine.begin() as conn:
    await conn.run_sync(Base.metadata.create_all)
