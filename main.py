from sys import int_info
from typing import Optional, Union
from fastapi import FastAPI, Header
from pydantic import BaseModel

banco_dados = []

class Item(BaseModel):
    quantidade: int
    valor: float

app = FastAPI()

@app.post("/item")
def adicionar_item(item: Item):
    banco_dados.append(item)
    return item
    #dar append no banco de dados com item e retornar o item

"""
@app.post("/")
def read_root(user_agent:Optional [str] = Header(None)):
    return {"Hello": "World"}
"""

@app.get("/items/{item_quantidade}")
def read_item(item_quantidade: int):
    return {"item_quantidade": item_quantidade}

@app.get("/items/{item_valor}")
def read_item(item_valor: float):
    return {"item_valor": item_valor}


@app.post("/item")
def add_item(novo_item: Item):
    valor_total = 0
    for item in banco_dados:
        valor_total += item.valor
        # realizar a soma 
    return valor_total


