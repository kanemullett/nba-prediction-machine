from service.data_scraping_service import DataScrapingService
from fastapi import FastAPI


app = FastAPI()
data_scraping_service = DataScrapingService()


@app.get("/scrape")
async def scrape() -> None:
    data_scraping_service.scrape()
