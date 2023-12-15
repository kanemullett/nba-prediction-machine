from pydantic import BaseModel
from typing import Any


class GameEvent(BaseModel):
    month: str
    year: int
    time: str
    away_team: str
    away_points: int
    home_team: str
    home_points: int
    attendance: str
    venue: str


class EventResponse(BaseModel):
    records: list[Any]
    record_count: int
