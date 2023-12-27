import os
from typing import Annotated
from fastapi import Depends, FastAPI
from sqlalchemy import create_engine

from kkbox1227.KkboxClient import KkboxClient
from kkbox1227.dto import Chart, ChartsResponseDto, Track, TracksResponseDto

engine = create_engine(os.environ["DATABASE_URL"])

app = FastAPI(debug=True)

def create_kkbox_client() -> KkboxClient:
    return KkboxClient(os.environ["KKBOX_CLIENT_ID"], os.environ["KKBOX_CLIENT_SECRET"])

@app.get("/charts")
async def charts(kkbox: Annotated[KkboxClient, Depends(create_kkbox_client)]) -> ChartsResponseDto:
    charts = list[Chart]()
    for item in kkbox.get_charts()["data"]:
        charts.append(Chart(id=item["id"], title=item["title"], url=item["url"]))

    return ChartsResponseDto(charts=charts)

@app.get("/charts/{chart_id}/tracks")
async def tracks(chart_id: str, kkbox: Annotated[KkboxClient, Depends(create_kkbox_client)]):
    tracks = list[Track]()
    for item in kkbox.get_track_from_chart(chart_id)["data"]:
        tracks.append(Track(id=item["id"], isrc=item["isrc"], name=item["name"], track_number=item["track_number"], url=item["url"]))

    return TracksResponseDto(tracks=tracks)
