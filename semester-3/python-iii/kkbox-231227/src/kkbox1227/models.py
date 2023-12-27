from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase): pass

class Chart(Base):
    __tablename__ = "charts"
    id: Mapped[str] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column()
    url: Mapped[str] = mapped_column()
    tracks: Mapped[list["Track"]] = relationship("Track", back_populates="chart")


class Track(Base):
    __tablename__ = "tracks"
    id: Mapped[str] = mapped_column(primary_key=True)
    isrc: Mapped[str] = mapped_column()
    name: Mapped[str] = mapped_column()
    track_number: Mapped[int] = mapped_column()
    url: Mapped[str] = mapped_column()
    chart_id: Mapped[str] = mapped_column(ForeignKey("charts.id"))
