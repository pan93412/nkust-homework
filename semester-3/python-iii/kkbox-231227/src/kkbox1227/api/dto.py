from pydantic import BaseModel


class Chart(BaseModel):
    id: str
    title: str
    url: str


class ChartsResponseDto(BaseModel):
    charts: list[Chart]


class Track(BaseModel):
    id: str
    isrc: str
    name: str
    track_number: int
    url: str


class TracksResponseDto(BaseModel):
    tracks: list[Track]
