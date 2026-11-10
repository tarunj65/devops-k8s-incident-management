from datetime import datetime

from sqlalchemy import DateTime, Integer, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base

class Incident(Base):
    __tablename__ = "incidents"

    id: Mapped[int] = mapped_column(
                Integer,
                primary_key=True,
                index=True
    )

    title: Mapped[str] = mapped_column(
                String(200),
                nullable=False
    )

    description: Mapped[str] = mapped_column(
                Text,
                nullable=False
    )

    category: Mapped[str] = mapped_column(
                String(50),
                nullable=False
    )

    priority: Mapped[str] = mapped_column(
                String(20),
                nullable=False
    )

    status: Mapped[str] = mapped_column(
                String(20),
                default="Open",
                nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
                DateTime(timezone=True),
                server_default=func.now(),
                nullable=False
    )
