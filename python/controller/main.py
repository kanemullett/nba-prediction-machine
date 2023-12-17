from fastapi import FastAPI
import controller.data_scraping_controller as data_scraping_controller

app = FastAPI()

app.include_router(data_scraping_controller.router)
