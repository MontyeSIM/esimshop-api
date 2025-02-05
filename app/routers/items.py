from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(
    prefix="/items",
    tags=["items"]
)

class Item(BaseModel):
    name: str
    description: str | None = None

@router.get("/")
async def get_items():
    return {"items": []}

@router.post("/")
async def create_item(item: Item):
    return item
