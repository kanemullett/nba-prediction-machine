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


@scrape.get("/scrape/stats")
async def scrape_stats(team: str) -> EventResponse:
    return data_scraping_service.scrape_stats(team)
