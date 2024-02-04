from typing import Union
from fastapi import FastAPI
from stardew_valley.database import Database
import pymysql

from stardew_valley.service.stardew_valley_service import StardewValleyService

app = FastAPI()

def on_startup():
    pymysql.install_as_MySQLdb()
    database = Database()
    database.init_database()

app.add_event_handler("startup", on_startup)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/allCollections")
def find_all_collections():
    return StardewValleyService().findAllCollections()

@app.get("/allVillager")
def find_all_villagers():
    pass

@app.get("/plantableCollection")
def find_plantable_collection():
    pass