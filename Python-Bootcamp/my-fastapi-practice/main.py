from fastapi import FastAPI

app = FastAPI()
items = [
    {"id": 1, "name": "Issue 1", "status": "open"},
    {"id": 2, "name": "Issue 2", "status": "closed"},
    {"id": 3, "name": "Issue 3", "status": "in progress"},
]
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

# Getting list items
@app.get("/items")
def read_items():
    return {"items": items}
@app.post("/items/insert")
def create_items():
    return {"items": items}
