from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI application!"}


@app.get("/greeting/{name}")
def read_greeting(name: str):
    return {"Hello, how are u ": name}

@app.get("/greeting")
def read_greeting(name: str):
    return {"Hello, hello ": name}

@app.post("/greet")
def greeting(name: str):
    return {"post, hello ": name}
