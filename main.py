from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# TODO 1: Create a GET route at "/"
# that returns {"message": "Hello FastAPI!"}

# TODO 2: Create a GET route at "/greet/{name}"
# that returns {"greeting": "Hello <name>!"}

# TODO 3: Create a POST route at "/square"
# that takes {"num": 4} and returns {"result": 16}


# Example model for TODO 3
class Number(BaseModel):
    num: int
