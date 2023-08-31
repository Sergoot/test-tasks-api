from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.db import Base


class Role(Base):
    """ Роль пользователя в системе """
    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(String(16))
    user: Mapped[list["User"]] = relationship(back_populates="role")


class User(Base):
    
    id: Mapped[int] = mapped_column(primary_key=True)

    email: Mapped[str] = mapped_column(String(32), unique=True, nullable=False)

    first_name: Mapped[str] = mapped_column(String(16))
    second_name: Mapped[str] = mapped_column(String(16))
    last_name: Mapped[str] = mapped_column(String(16))

    role_id: Mapped[int] = mapped_column(ForeignKey("role.id"))
    role: Mapped["Role"] = relationship(back_populates="user")