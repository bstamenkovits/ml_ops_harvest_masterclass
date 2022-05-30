import os
import logging

from fastapi import FastAPI

from model_api.routers import basic_router

if not os.path.isdir("logs"):
    os.mkdir("logs")

logging.basicConfig(filename="./logs/logfile.log",
                    filemode="a",
                    format="%(levelname)s %(asctime)s - %(message)s",
                    level=logging.INFO)

logger = logging.getLogger()

app = FastAPI()

app.include_router(basic_router.router)


@app.get("/")
async def root():
    return {"message": "Welcome to the simple API."}


def restart_api():
    os.system('sh start_api.sh')
