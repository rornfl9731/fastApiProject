from fastapi import FastAPI
from sqlalchemy.orm import declarative_base
from pydantic import BaseModel

app = FastAPI()
Base = declarative_base()


class Item(BaseModel):
    name: str
    number: int


@app.post("/")
async def first_post(item : Item):
    print(item)
    return item
@app.get("/")
async def first():
    hi='hi'
    return hi


