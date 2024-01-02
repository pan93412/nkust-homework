from typing import Optional
from pydantic import BaseModel


class ChartDto(BaseModel):
    id: str


class TrackDto(BaseModel):
    id: str
    name: str
    artist: str


class TrackUpdateDto(BaseModel):
    name: Optional[str] = None
    artist: Optional[str] = None
