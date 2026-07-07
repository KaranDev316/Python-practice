from fastapi import FastAPI

app = FastAPI(
    title="Notes API",
    version="1.0.0",
    description="A mini Note API built with FastAPI",
)


@app.get("/health")
def health_check():
    return {"status": "ok"}