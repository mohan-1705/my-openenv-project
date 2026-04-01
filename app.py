from fastapi import FastAPI
from env import SimpleEnv

app = FastAPI()

@app.get("/")
def run_env():
    env = SimpleEnv()
    state = env.reset()

    results = []

    for i in range(5):
        action = "increase"
        state, reward, done, _ = env.step(action)
        results.append({
            "step": i,
            "state": state,
            "reward": reward
        })
        if done:
            break

    return {"output": results}
