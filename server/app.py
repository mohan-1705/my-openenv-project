from fastapi import FastAPI
from env import MyEnv
import uvicorn

app = FastAPI()
env = MyEnv()

@app.get("/")
def home():
    return {"message": "API Running"}

@app.post("/reset")
def reset():
    return env.reset()

@app.post("/step")
def step():
    state, reward, done, _ = env.step()
    return {
        "state": state,
        "reward": reward,
        "done": done
    }

# ✅ IMPORTANT MAIN FUNCTION
def main():
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860)

# ✅ REQUIRED FOR VALIDATION
if __name__ == "__main__":
    main()
