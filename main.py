from typing import Dict
from fastapi import FastAPI
app = FastAPI()

@app.get('/')
def root():
    return {'message': 'Hello world, from Galileo Master!! Section V'}

@app.get('/items/{item_id}')
def read_item(item_id: int) -> Dict[str, int]:
    return {'item_id':item_id}
