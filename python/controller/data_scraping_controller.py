from fastapi import FastAPI
from model.models import EventResponse
from service.data_scraping_service import DataScrapingService


scrape = FastAPI()
data_scraping_service = DataScrapingService()


@scrape.get("/scrape/games")
async def scrape_games(month: str, year: int) -> EventResponse:
    """
    Scrape games for a given month & year combination.

    :param month: The month within the season.
    :param year: The year the games took place in.
    :return: Scraped games.
    """
    return data_scraping_service.scrape_games(month, year)


@scrape.get("/scrape/stats/team")
async def scrape_team_stats(team: str) -> EventResponse:
    """
    Scrape a team's stats for every season in the NBA's three point era (1979-80 onwards).

    :param team: The team's three letter abbreviation.
    :return: Scraped team stats.
    """
    return data_scraping_service.scrape_team_stats(team)


@scrape.get("/scrape/stats/opponent")
async def scrape_opponent_stats(team: str) -> EventResponse:
    """
    Scrape a team's opponent stats for every season in the NBA's three point era (1979-80 onwards).

    :param team: The team's three letter abbreviation.
    :return: Scraped opponent stats.
    """
    return data_scraping_service.scrape_opponent_stats(team)
