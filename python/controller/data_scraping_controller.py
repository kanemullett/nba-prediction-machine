from fastapi import FastAPI
from model.models import EventResponse
from service.data_scraping_service import DataScrapingService


scrape = FastAPI()
data_scraping_service = DataScrapingService()


@scrape.get("/scrape/games")
async def scrape_games(month: str, year: int) -> EventResponse:
    return data_scraping_service.scrape_games(month, year)
