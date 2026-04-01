from fastapi import FastAPI
from env import MyEnv

app = FastAPI()
env = MyEnv()

@app.get("/")
def home():
    return {"message": "API Running"}

@app.post("/reset")
def reset():
    return {"state": env.reset()}

@app.post("/step")
def step():
    state, reward, done, _ = env.step()
    return {
        "state": state,
        "reward": reward,
        "done": done
    }
