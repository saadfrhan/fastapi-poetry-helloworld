from fastapi import FastAPI
from uvicorn import run

# Create an instance of FastAPI
app = FastAPI(
    title="Greeting API",
    description="A greeting API to greet you at different times of the day!",
    version="1.0.0",
    docs_url="/documentation",
    redoc_url="/redoc",
)

# Define a route for the homepage
@app.get("/")
def welcome():
    return {"message": "Hey friend! Welcome to our wonderful world!"}

# Define a route for morning greetings
@app.get("/morning")
def morning():
    return {"message": "Good morning sunshine! ☀️"}

# Define a route for nighttime greetings
@app.get("/night")
def night():
    return {"message": "Good night, sleep tight! 🌙"}

# Define a function for starting the app
def start():
    """Launched with `poetry run start` at root level"""
    run("fastapi_poetry_helloworld.main:app", host="0.0.0.0", port=8000, reload=True)
