from fastapi import FastAPI
from env import SimpleEnv

app = FastAPI()
env = SimpleEnv()

@app.post("/reset")
def reset():
    state = env.reset()
    return {"state": state}

@app.post("/step")
def step(action: dict):
    result = env.step(action.get("action", 1))
    return result

@app.get("/state")
def get_state():
    return {"state": env.state}
