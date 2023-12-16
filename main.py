from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Item
from schemas import ItemSchema






app = FastAPI()

@app.get('/')
def events():
    return {"message:" "Code Check Onetwo"}

@app.get('/items')
def events(db: Session = Depends(get_db)):
    items = db.query(Item).all()
    return items

@app.get('/items/{item_id}')
def event():
    return {}

@app.post('/items')
def create_event(item: ItemSchema):
    print(item) 
    return {"Item Created Succesfully"}

@app.patch('/items/{item_id}')
def update_event(item_id: int):
    return {f"Item {item_id} created succesfully"}

@app.delete('/items/{item_id}')
def delete_event(item_id: int):
    return {f"Itemt {item_id} created succesfully"}

