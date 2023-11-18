from sqlalchemy import BigInteger, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column, DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

from typing import List

from config import DATABASE_URL

engine = create_async_engine(DATABASE_URL, echo=True)

async_session = async_sessionmaker(engine)

class Base(AsyncAttrs, DeclarativeBase):
  pass

class User(Base):
  __tablename__ = 'user_table'

  id: Mapped[int] = mapped_column(primary_key=True)
  tg_id: Mapped[int] = mapped_column(BigInteger)
  fio: Mapped[str] = mapped_column(String)
  phone_numebr: Mapped[str] = mapped_column(String)
  requests: Mapped[List['Request']] = relationship(back_populates="user")

class Request(Base):
  __tablename__ = 'request_table'

  id: Mapped[int] = mapped_column(primary_key=True)
  description: Mapped[str] = mapped_column(String)
  address: Mapped[str] = mapped_column(String)
  category: Mapped[str] = mapped_column(String)
  date: Mapped[str] = mapped_column(String)
  time: Mapped[str] = mapped_column(String)
  cost_min: Mapped[int] = mapped_column(Integer)
  cost_max: Mapped[int] = mapped_column(Integer)
  user_id: Mapped[int] = mapped_column(ForeignKey('user_table.id'))
  user: Mapped["User"] = relationship(back_populates='requests')


async def async_main():
  async with engine.begin() as conn:
    await conn.run_sync(Base.metadata.create_all)

