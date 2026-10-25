from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI application!"}


@app.get("/greeting/{name}")
def read_greeting(name: str):
    return {"Hello, how are u ": name}