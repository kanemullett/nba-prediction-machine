from enum import Enum
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


class StatsEventType(Enum):
    TEAM = "TEAM"
    OPPONENT = "OPPONENT"


class StatsEvent(BaseModel):
    team: str
    season: str
    wins: int
    losses: int
    division_position: int
    average_age: float | None
    average_height: str | None
    average_weight: int | None
    games_played: int
    minutes_per_game: float
    field_goals_per_game: float
    field_goal_attempts_per_game: float
    field_goal_percentage: float
    three_pointers_per_game: float
    three_point_attempts_per_game: float
    three_point_percentage: float
    two_pointers_per_game: float
    two_point_attempts_per_game: float
    two_point_percentage: float
    free_throws_per_game: float
    free_throw_attempts_per_game: float
    free_throw_percentage: float
    offensive_rebounds_per_game: float
    defensive_rebounds_per_game: float
    total_rebounds_per_game: float
    assists_per_game: float
    steals_per_game: float
    blocks_per_game: float
    turnovers_per_game: float
    personal_fouls_per_game: float
    points_per_game: float


class EventResponse(BaseModel):
    records: list[Any]
    record_count: int
