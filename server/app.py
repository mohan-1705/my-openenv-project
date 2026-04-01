from fastapi import FastAPI
from env import SimpleEnv

app = FastAPI()
env = SimpleEnv()

@app.get("/")
def home():
    return {"message": "API Running"}

@app.post("/reset")
def reset():
    return {"state": env.reset()}

@app.post("/step")
def step():
    return env.step()


@app.get("/tasks")
def tasks():
    return env.get_tasks()
