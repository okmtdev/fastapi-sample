from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from base import BaseORM


class Pet(BaseORM):
    __tablename__ = "pets"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(64))
    age: Mapped[int] = mapped_column(Integer)

    def __repr__(self):
        return "<Pet('id={}', name={}, age={})>".format(self.id, self.name, self.age)
