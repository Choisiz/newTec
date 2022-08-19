from fastapi import FastAPI

from fastapi.responses import FileResponse

from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def hello():
    return FileResponse('index.html')

class Item(BaseModel):
    name: str
    price: float
    

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id,}

@app.post("/items/{item_id}")
def update_item(item_id: int, data:Item):
    print(data)
    return {'이름':data.name,'가격':data.price,"item_id": item_id}

@app.get('/tip')
def hello2():
    return {'재밌는기능':'/redoc나docs쓰면 만든함수 및 리턴값나옴'}
