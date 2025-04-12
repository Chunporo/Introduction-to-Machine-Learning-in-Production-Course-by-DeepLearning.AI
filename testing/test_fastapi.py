from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    is_offer: Union[bool, None] = None
@app.get("/")
async def read_root():
    """
    Handle GET requests to the root endpoint and return a greeting message.

    Returns:
        dict: A dictionary containing a simple greeting message.
    """
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    """
    Handle GET requests to the items endpoint and return the item_id and query parameters.

    Args:
        item_id (int): The identifier of the item.
        q (Union[str, None]): An optional query parameter.

    Returns:
        dict: A dictionary containing the item_id and query parameters.
    """
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    """
    Handle PUT requests to update an item.

    Args:
        item_id (int): The identifier of the item.
        item (Item): The item data to be updated.

    Returns:
        dict: A dictionary containing the updated item data.
    """
    return {"item_name": item.name, "item_id": item_id}