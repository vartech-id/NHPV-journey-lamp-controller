from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Users(Base):
    __tablename__ = "couples"

    id: Mapped[int] = mapped_column(primary_key=True)
    pria: Mapped[str] = mapped_column(String)
    wanita: Mapped[str] = mapped_column(String)

    def __repr__(self) -> str:
        return f"Users(id={self.id}, pria={self.pria}, wanita={self.wanita})"
