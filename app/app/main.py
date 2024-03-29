from fastapi import FastAPI

from routers import post

app = FastAPI()

app.include_router(post.router)


@app.get("/")
def root():
    return {"message": "Hello World"}