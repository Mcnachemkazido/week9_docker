from fastapi import FastAPI
import uvicorn
import json
from pathlib import Path
from pydantic import BaseModel


DB_PATH= Path("./db/shopping_list.json")
BACKUP_DATA_PATH = Path('./data/backup_shopping_list.json')



def load_database(path):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        raise ValueError("Database file is not valid JSON.")


def save_database(data,path) -> None:
    with open(path, "w") as f:
        json.dump(data, f, indent=2)


def check_database_exists() -> None:
    if not DB_PATH.exists():
        print("We are sorry, the database does not exist.")
        raise FileNotFoundError
    else:
        print("Everything is fine, the data exists.")


app = FastAPI()


class Item(BaseModel):
    name: str
    quantity: int

@app.on_event("startup")
def startup_event():
    return check_database_exists()


@app.get("/items/")
def get_items():
    return load_database(DB_PATH)


@app.post("/items/")
def post_item(item:Item):
    data = load_database(DB_PATH)
    item_id = len(data) + 1
    item = {"id":item_id,"name":item.name,"quantity":item.quantity}
    data.append(item)
    save_database(data,DB_PATH)
    print()
    return {"message":"The item has been successfully added"}


@app.get("/backup")
def get_backup():
    if BACKUP_DATA_PATH.exists():
        return load_database(BACKUP_DATA_PATH)
    else:
        return {"massage":"file not exists"}

@app.post("/backup/save")
def save_volume_to_backup():
    backup_data = load_database(DB_PATH)
    save_database(backup_data,BACKUP_DATA_PATH)
    return {"massage":"Writing to the local page was successful"}




