from fastapi import FastAPI
import uvicorn
import json
from pathlib import Path
from pydantic import BaseModel


DB_PATH= Path("./db/shopping_list.json")

def load_database():
    try:
        with open(DB_PATH, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        raise ValueError("Database file is not valid JSON.")


def save_database(data) -> None:
    with open(DB_PATH, "w") as f:
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
    return load_database()


@app.post("/items/")
def post_item(item:Item):
    data = load_database()
    item_id = len(data) + 1
    item = {"id":item_id,"name":item.name,"quantity":item.quantity}
    data.append(item)
    save_database(data)
    print()
    return {"message":"The item has been successfully added"}







