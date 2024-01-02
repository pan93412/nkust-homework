from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase): pass

class Chart(Base):
    __tablename__ = "charts"
    id: Mapped[str] = mapped_column(String(40), primary_key=True)
    tracks: Mapped[list["Track"]] = relationship("Track")


class Track(Base):
    __tablename__ = "tracks"
    id: Mapped[str] = mapped_column(String(40), primary_key=True)
    name: Mapped[str] = mapped_column(String(256))
    artist: Mapped[str] = mapped_column(String(256))
    chart_id: Mapped[str] = mapped_column(String(40), ForeignKey("charts.id"))
