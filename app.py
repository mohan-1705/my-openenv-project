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
def step(action: dict):
    return env.step(action.get("action", 1))

@app.get("/state")
def state():
    return {"state": env.state}
