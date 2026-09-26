from pydantic import BaseModel


class ChaiItem(BaseModel):
    id: int
    name: str
    category: str
    price: float
    description: str
    available: bool


class ChaiItemResponse(BaseModel):
    status: str = "success"
    count: int
    items: list[ChaiItem]
