# 🧩 FASTAPI Demo Lab

A super simple FastAPI demo you can complete in under 5 minutes!

---

## 🚀 Setup Instructions

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Run the app
```bash
uvicorn main:app --reload
```

### 3️⃣ Open your browser
Go to: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🧠 TODO Tasks

Edit **main.py** and complete:

1. **Create a GET route** at `/` that returns:
   ```python
   {"message": "Hello FastAPI!"}
   ```

2. **Create a GET route** at `/greet/{name}` that returns:
   ```python
   {"greeting": "Hello <name>!"}
   ```

3. **Create a POST route** at `/square` that takes JSON like:
   ```json
   {"num": 4}
   ```
   and returns:
   ```json
   {"result": 16}
   ```

---

## ✅ Test Your API

Use **Swagger UI** to test your endpoints:
```
http://127.0.0.1:8000/docs
```

Or use **curl**:
```bash
curl http://127.0.0.1:8000/
curl http://127.0.0.1:8000/greet/Kevin
curl -X POST -H "Content-Type: application/json" -d '{"num": 4}' http://127.0.0.1:8000/square
```

---

## 💡 Full Answers (Instructor Reference)

Here’s the fully completed **main.py**:

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello FastAPI!"}

@app.get("/greet/{name}")
def greet_name(name: str):
    return {"greeting": f"Hello {name}!"}

@app.get("/square/{number}")
def square_get(number: int):
    """Allows GET /square/<number> so the endpoint is usable from a browser."""
    return {"result": number ** 2}
```

---

✅ **Expected Outputs**
| Endpoint | Method | Input | Output |
|-----------|---------|--------|--------|
| `/` | GET | – | `{"message": "Hello FastAPI!"}` |
| `/greet/Kevin` | GET | – | `{"greeting": "Hello Kevin!"}` |
| `/square` | POST | `{"num": 4}` | `{"result": 16}` |

---

🧩 **Goal:** Practice FastAPI basics — routes, path parameters, and JSON request bodies.
