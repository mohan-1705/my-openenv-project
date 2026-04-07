import os
from openai import OpenAI
from env import SimpleEnv

print("START")

# Load environment variables
API_BASE_URL = os.getenv("API_BASE_URL")
MODEL_NAME = os.getenv("MODEL_NAME")
HF_TOKEN = os.getenv("HF_TOKEN")

print("STEP: Environment variables loaded")

# Initialize OpenAI client
client = OpenAI(
    base_url=API_BASE_URL,
    api_key=HF_TOKEN
)

print("STEP: OpenAI client initialized")

# Initialize environment
env = SimpleEnv()
state = env.reset()

print("STEP: Environment initialized")

# Run agent loop
for i in range(5):
    # Simple LLM-based decision (or keep baseline if needed)
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "user", "content": f"State is {state}. What action should I take?"}
        ]
    )

    action = response.choices[0].message.content.strip()

    state, reward, done, _ = env.step(action)

    print(f"STEP: Step {i}, Action: {action}, State: {state}, Reward: {reward}")

    if done:
        break

print("END")
