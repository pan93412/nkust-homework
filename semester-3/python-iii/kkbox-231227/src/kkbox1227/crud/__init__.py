import os
from fastapi import Depends, FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from kkbox1227.KkboxClient import KkboxClient
from kkbox1227.crud.dto import ChartDto, TrackDto, TrackUpdateDto
from kkbox1227.crud.models import Base, Chart, Track

app = FastAPI(debug=True)
engine = create_engine(os.environ["DATABASE_URL"])

def create_kkbox_client() -> KkboxClient:
    return KkboxClient(os.environ["KKBOX_CLIENT_ID"], os.environ["KKBOX_CLIENT_SECRET"])

def get_session():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()


with Session(engine) as session:
    Base.metadata.create_all(engine)
    session.commit()


@app.post("/charts/{chart_id}/init")
def chart_init(chart_id: str, kkbox_client: KkboxClient = Depends(create_kkbox_client), session: Session = Depends(get_session)):
    if session.query(Chart).filter(Chart.id == chart_id).first() is not None:
        return {"message": "Chart already initialized."}

    chart = Chart(id=chart_id)
    session.add(chart)
    session.commit()

    tracks = (
        Track(id=track["id"], name=track["name"], artist=track["album"]["artist"]["name"], chart_id=chart_id)
        for track in kkbox_client.get_track_from_chart(chart_id)["data"]
    )
    session.add_all(tracks)
    session.commit()
    return {"message": "Database initialized."}


@app.get("/charts")
def charts(session: Session = Depends(get_session)) -> list[ChartDto]:
    raw_charts = session.query(Chart).all()
    dto_charts = [
        ChartDto(id=chart.id)
        for chart in raw_charts
    ]

    return dto_charts


@app.get("/charts/{chart_id}/tracks")
def tracks(chart_id: str, session: Session = Depends(get_session)) -> list[TrackDto]:
    raw_tracks = session.query(Track).filter(Track.chart_id == chart_id).all()
    dto_tracks = [
        TrackDto(id=track.id, name=track.name, artist=track.artist)
        for track in raw_tracks
    ]

    return dto_tracks

@app.patch("/charts/{chart_id}/tracks/{track_id}")
def track_update(chart_id: str, track_id: str, patch: TrackUpdateDto, session: Session = Depends(get_session)):
    track = session.query(Track).filter(Track.id == track_id, Chart.id == chart_id).first()
    if track is None:
        return {"message": "Track not found."}

    track.name = patch.name or track.name
    track.artist = patch.artist or track.artist

    session.commit()
    return {"message": "Track updated."}

@app.delete("/charts/{chart_id}/tracks/{track_id}")
def track_delete(chart_id: str, track_id: str, session: Session = Depends(get_session)):
    track = session.query(Track).filter(Track.id == track_id, Chart.id == chart_id).first()
    if track is None:
        return {"message": "Track not found."}

    session.delete(track)
    session.commit()
    return {"message": "Track deleted."}
