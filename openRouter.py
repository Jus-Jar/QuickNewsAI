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


def summarizerAgentRequest(message,client):

    prompt = f"Condense this into short summary paragraphs: {message}"

    completion = client.chat.completions.create(
    model="meta-llama/llama-3.2-3b-instruct:free",
    messages=[
        {
        "role": "user",
        "content": prompt
        }
    ]
    )
    return completion.choices[0].message.content

def searchInputAgentRequest(message,client):

    prompt = f" You are QuickNewsAI a chatbot that returns only summarized news articles. Reject any search that differ from this purpose with a message starting with 'Sorry'. Take this prompt and return only a single relevant search query for a web search engine: {message}"

    completion = client.chat.completions.create(
    model="meta-llama/llama-3.2-3b-instruct:free",
    messages=[
        {
        "role": "user",
        "content": prompt
        }
    ]
    )
    return completion.choices[0].message.content

def responseAgentRequest(prompt,data,client):

    prompt = f"You are QuickNewsAI a chatbot that returns only summarized news articles. Respond to this prompt {prompt} in as a short article using this data: {data}"

    completion = client.chat.completions.create(
    model="meta-llama/llama-3.2-3b-instruct:free",
    messages=[
        {
        "role": "user",
        "content": prompt
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



import requests

# Define the API endpoint
url = 'https://openrouter.ai/api/v1/auth/key'

# Define the headers, replace $OPENROUTER_API_KEY with your actual API key
headers = {
    'Authorization': "Bearer " + os.getenv("OPENROUTER_API_KEY")
}

# Make the GET request
response = requests.get(url, headers=headers)

# Check the response status
if response.status_code == 200:
    # If the request was successful, print the result
    print(response.json())  # Assuming the response is in JSON format
else:
    # If there was an error, print the status code and error message
    print(f"Error: {response.status_code}, {response.text}")




# message = "I want to know the latest russia vs ukraine news"
# print(searchInputAgentRequest(message, loadOpenRouterClient()))