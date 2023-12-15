from bs4 import BeautifulSoup
from model.models import EventResponse, GameEvent
from requests import get


class DataScrapingService:
    @staticmethod
    def scrape(month: str, year: int) -> EventResponse:
        url = f"https://www.basketball-reference.com/leagues/NBA_{year}_games-{month}.html"
        page = get(url)

        soup = BeautifulSoup(page.content, "html.parser")

        table_rows = soup.find_all("tr")

        row_elements = list(filter(lambda n: len(n) > 0, list(map(lambda n: n.find_all("td"), table_rows))))

        row_values = []

        for element in row_elements:
            row_values.append(list(map(lambda n: n.text, element)))

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
