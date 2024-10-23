import os 
from dotenv import load_dotenv

from groq import Groq

#Note that the Groq API is currently free as it is in beta however they plan to be a price tier service when they do become official

# Load the variables from .env into the environment
load_dotenv()


def loadGroqClient():
    client = Groq(
        api_key=os.getenv("GROQ_API_KEY"),
    )
    return client

def groqMessageRequest(message,client):

    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": message,
        }
    ],
    model="llama-3.1-8b-instant",
    )

    return chat_completion.choices[0].message.content



def loadSummarizerClient(request):
    client = loadGroqClient()

