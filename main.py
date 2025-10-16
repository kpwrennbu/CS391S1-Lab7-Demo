from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# TODO 1: Create a GET route at "/"
# that returns {"message": "Hello FastAPI!"}
@app.get("/")
def read_root():
    return {"message": "Hello FastAPI!"}
# TODO 2: Create a GET route at "/greet/{name}"
# that returns {"greeting": "Hello <name>!"}
@app.get("/greet/{name}")
def greet_name(name: str):
    return {"greeting": f"Hello {name}!"}
# TODO 3: Create a GET route at "/square"
# that takes {"num": 4} and returns {"result": 16}
@app.get("/square/{number}")
def square_get(number: int):
    """Allows GET /square/<number> so the endpoint is usable from a browser."""
    return {"result": number ** 2}
