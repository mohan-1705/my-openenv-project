import os
from openai import OpenAI

print("START")

# Load environment variables
API_BASE_URL = os.getenv("API_BASE_URL")
MODEL_NAME = os.getenv("MODEL_NAME")
HF_TOKEN = os.getenv("HF_TOKEN")

print("STEP: Environment variables loaded")

# Initialize client
client = OpenAI(
    base_url=API_BASE_URL,
    api_key=HF_TOKEN
)

print("STEP: Client initialized")

# Run inference
response = client.chat.completions.create(
    model=MODEL_NAME,
    messages=[
        {"role": "user", "content": "Hello"}
    ]
)

print("STEP: Response generated")

print(response.choices[0].message.content)

print("END")
