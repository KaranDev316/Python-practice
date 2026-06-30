from fastapi import FastAPI

app = FastAPI()
items = [
    {"id": 1, "name": "item 1"},
    {"id": 2, "name": "item 2"},
    {"id": 3, "name": "item 3"},

]
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

# Getting list items
@app.get("/items")
def read_items():
    return {"items": items}
