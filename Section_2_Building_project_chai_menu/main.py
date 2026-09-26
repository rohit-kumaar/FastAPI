from models import ChaiItemResponse, ChaiItem
from data import chai_data
from fastapi import FastAPI, Query, HTTPException

app = FastAPI(
    title="Menu App",
    description="This is a menu app"
)

@app.get("/")
def root():
    return {
        "message" : "Working",
    }

@app.get("/menu", response_model=ChaiItemResponse)
def get_menu(category: str | None = Query(None, description="Filter by chai, snaks or combo")):
    if category:
        items = [item for item in chai_data if item["category"].lower() == category.lower()]
        if not items:
            raise HTTPException(status_code=404, detail="Item not found")

        return ChaiItemResponse(
            status="success",
            count=len(items),
            items=items
        )

    return ChaiItemResponse(
            status="success",
            count=len(chai_data),
            items=chai_data
    )

@app.get("/menu/{item_id}", response_model=ChaiItem)
def get_item(item_id: int):
    for item in chai_data:
        if item["id"] == item_id:
            return item

    raise HTTPException(status_code=404, detail=f"Menu item with id {item_id} not found")    