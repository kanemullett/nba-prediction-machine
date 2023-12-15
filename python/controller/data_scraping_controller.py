from fastapi import FastAPI
from model.models import EventResponse
from service.data_scraping_service import DataScrapingService


app = FastAPI()
data_scraping_service = DataScrapingService()


@app.get("/scrape")
async def scrape(month: str, year: int) -> EventResponse:
    return data_scraping_service.scrape(month, year)
