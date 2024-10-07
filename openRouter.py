import os
from openai import OpenAI
from dotenv import load_dotenv

# Load the variables from .env into the environment
load_dotenv()

# gets API Key from environment variable OPENAI_API_KEY
def loadOpenRouterClient():
    client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    )
    return client

def llamaMessageRequest(message,client):
    completion = client.chat.completions.create(
    model="meta-llama/llama-3.2-3b-instruct:free",
    messages=[
        {
        "role": "user",
        "content": message
        }
    ]
    )
    return completion.choices[0].message.content

def liquidMessageRequest(message,client):
    completion = client.chat.completions.create(
    model="liquid/lfm-40b",
    messages=[
        {
        "role": "user",
        "content": message
        }
    ]
    )
    return completion.choices[0].message.content