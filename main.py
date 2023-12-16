from fastapi import FastAPI
from schemas import ItemSchema





app = FastAPI()

@app.get('/')
def events():
    return {"message:" "Code Check Onetwo"}

@app.get('/items/{item_id}')
def event():
    return {}

@app.post('/items')
def create_event(item: ItemSchema):
    print(item)
    return {"Events Created Succesfully"}

@app.patch('/items/{item_id}')
def update_event(item_id: int):
    return {f"Event {item_id} created succesfully"}

@app.delete('/items/{item_id}')
def delete_event(item_id: int):
    return {f"Event {item_id} created succesfully"}

