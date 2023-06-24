from http.client import HTTPException
from typing import Union

from fastapi import FastAPI, Query

from .database import SessionLocal
from .models import ItemModel, ItemSchema


app = FastAPI()
db = SessionLocal()


@app.get("/")
def read_root():
    query = db.query(ItemModel)
    items = query.all()
    db.close()
    items_list = [ItemSchema.from_orm(item).dict() for item in items]
    return items_list


@app.post("/items")
def create_item(name: str, description: str):
    item = ItemModel(name=name, description=description)
    db.add(item)
    db.commit()
    db.close()
    item = {"name": name, "description": description}
    return item

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    item = db.query(ItemModel).filter(ItemModel.id == item_id).first()
    if item:
        db.delete(item)
        db.commit()
        return {
            "id": item.id,
            "name": item.name,
            "description": item.description,
            "message": "Item deleted successfully"
        }
    raise HTTPException(status_code=404, detail="Item not found")


@app.put("/items/{item_id}")
def update_item(item_id: int, name: str = Query(None), description: str = Query(None)):
    item = db.query(ItemModel).filter(ItemModel.id == item_id).first()
    if item:
        if name is not None:
            item.name = name
        if description is not None:
            item.description = description
        db.commit()
        db.refresh(item)
        db.close()
        return {"message": "Item updated successfully", "item": ItemSchema.from_orm(item).dict()}
    raise HTTPException(status_code=404, detail="Item not found")

@app.get("/items")
def get_items():
    try:
        query = db.query(ItemModel)
        items = query.all()
        db.close()
        return [ItemSchema.from_orm(item).dict() for item in items]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/items/{name}")
def search_item_name(name: str):
    try:
        query = db.query(ItemModel)
        if name:
            items = query.filter(ItemModel.name.ilike(f"%{name}%")).all()
            db.close()
            if not items:
                return {"message": "No items matching the search criteria were found."}
            return [ItemSchema.from_orm(item).dict() for item in items]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))