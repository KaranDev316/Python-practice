from fastapi import FastAPI, HTTPException,status
from starlette.responses import HTMLResponse

app = FastAPI()
dictionary = {
    "apple": "A round, crisp fruit with red or green skin.",
    "banana": "A long, curved fruit with a yellow peel.",
    "cherry": "A small, round, deep red fruit."
}
@app.get("/api/posts/{post_id}")
def get_post(post_id: str):
    if dictionary[post_id] == post_id:
            return dictionary[post_id]
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
@app.get("/api/posts/{post_id}",response_class=HTMLResponse)
def get_post_html(post_id: str):
    return
