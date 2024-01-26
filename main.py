from manager.load_config import CONFIG

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from contextlib import asynccontextmanager

from pymongo import MongoClient
from pymongo.server_api import ServerApi

import colorama
from colorama import Fore

colorama.init(autoreset=True)

@asynccontextmanager
async def lifespan(app: FastAPI):
    mongo_uri = f"mongodb+srv://{CONFIG['DB_USER']}:{CONFIG['DB_PASS']}@makerhackathon.o5ulesl.mongodb.net/?retryWrites=true&w=majority"
    app.state.mongoConnection = MongoClient(mongo_uri, server_api = ServerApi('1'))

    yield

    app.state.mongoConnection.close()

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(endpoints)
