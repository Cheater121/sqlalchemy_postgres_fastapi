import datetime

from sqlalchemy import BigInteger, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class ToDo(Base):
    __tablename__ = "todo"  # Указываем как будет называться наша таблица в базе данных (пишется в ед. числе)

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, index=True)  # Строка  говорит, что наша колонка будет интом, но уточняет, что ещё и большим интом (актуально для ТГ-ботов), первичным ключом и индексироваться
    description: Mapped[str]  # Описание, просто строка; если нужно дополнительные условия добавить, то mapped_column
    completed: Mapped[bool] = mapped_column(default=False)  # Задали значение по-умолчанию False
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now())  # просто для примера

# Код выше аналогичен этим устаревшим примерам:

# todo_list = Table("todo_list", metadata,
#                   Column("id", BigInteger, primary_key=True, index=True),
#                   Column("description", String),
#                   Column("completed", Boolean, default=False),
#                   Column("created_at", DateTime, nullable=False, default=func.utcnow())
#                   )

# class ToDo(Base):
#     __tablename__ = "todo"
#
#     id = Column(BigInteger, primary_key=True, index=True)
#     description = Column(String)
#     completed = Column(Boolean, default=False)
#     created_at = Column(DateTime, nullable=False, default=func.utcnow())
