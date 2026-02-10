from datetime import datetime
from sqlalchemy import DateTime, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Users(Base):
    __tablename__ = "couples"

    id: Mapped[int] = mapped_column(primary_key=True)
    pria: Mapped[str] = mapped_column(String)
    wanita: Mapped[str] = mapped_column(String)
    register_timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True))

    def __repr__(self) -> str:
        return (
            "Users("
            f"id={self.id}, pria={self.pria}, wanita={self.wanita}, "
            f"register_timestamp={self.register_timestamp}"
            ")"
        )
