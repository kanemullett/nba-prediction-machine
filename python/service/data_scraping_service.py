from bs4 import BeautifulSoup
from model.models import EventResponse, GameEvent, StatsEvent
from requests import get


class DataScrapingService:
    def scrape_games(self, month: str, year: int) -> EventResponse:
        """
        Scrape games for a given month & year combination.

        :param month: The month within the season.
        :param year: The year the games took place in.
        :return: Scraped games.
        """

        url = f"https://www.basketball-reference.com/leagues/NBA_{year}_games-{month}.html"

        row_values = self.__get_table_rows(url)

        game_events = []

        for row in row_values:
            game_events.append(
                GameEvent(
                    month=month,
                    year=year,
                    time=row[0],
                    away_team=row[1],
                    away_points=int(row[2]),
                    home_team=row[3],
                    home_points=int(row[4]),
                    attendance=row[7],
                    venue=row[8]
                )
            )

        return EventResponse(
            records=game_events,
            record_count=len(game_events)
        )

    def scrape_stats(self, team: str) -> EventResponse:
        url = f"https://www.basketball-reference.com/teams/{team.upper()}/stats_per_game_totals.html"

        table_rows = self.__get_table_rows(url)

        stat_events = []

        year = 2023

        for row in table_rows:
            if year == 1978:
                break
            stat_events.append(
                StatsEvent(
                    team=row[1],
                    season=self.__create_season_tag(year),
                    wins=int(row[2]),
                    losses=int(row[3]),
                    division_position=int(row[4]),
                    average_age=float(row[6]),
                    average_height=row[7],
                    average_weight=int(row[8]),
                    games_played=int(row[10]),
                    minutes_per_game=float(row[11]),
                    field_goals_per_game=float(row[12]),
                    field_goal_attempts_per_game=float(row[13]),
                    field_goal_percentage=float("0" + row[14]),
                    three_pointers_per_game=float(row[15]),
                    three_point_attempts_per_game=float(row[16]),
                    three_point_percentage=float("0"+ row[17]),
                    two_pointers_per_game=float(row[18]),
                    two_point_attempts_per_game=float(row[19]),
                    two_point_percentage=float("0" + row[20]),
                    free_throws_per_game=float(row[21]),
                    free_throw_attempts_per_game=float(row[22]),
                    free_throw_percentage=float("0" + row[23]),
                    offensive_rebounds_per_game=float(row[24]),
                    defensive_rebounds_per_game=float(row[25]),
                    total_rebounds_per_game=float(row[26]),
                    assists_per_game=float(row[27]),
                    steals_per_game=float(row[28]),
                    blocks_per_game=float(row[29]),
                    turnovers_per_game=float(row[30]),
                    personal_fouls_per_game=float(row[31]),
                    points_per_game=float(row[32])
                )
            )
            year -= 1

        return EventResponse(
            records=stat_events,
            record_count=len(stat_events)
        )

    @staticmethod
    def __create_season_tag(year: int) -> str:
        second_half = year + 1

        return f"{year}-{str(second_half)[-2:]}"

    @staticmethod
    def __get_table_rows(url: str) -> list:
        page = get(url)

        soup = BeautifulSoup(page.content, "html.parser")

        table_rows = soup.find_all("tr")

        row_elements = list(filter(lambda n: len(n) > 0, list(map(lambda n: n.find_all("td"), table_rows))))

        row_values = []

        for element in row_elements:
            row_values.append(list(map(lambda n: n.text, element)))

        return row_values
