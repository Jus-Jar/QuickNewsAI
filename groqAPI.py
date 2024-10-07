import os 
from dotenv import load_dotenv

from groq import Groq

#Note that the Groq API is currently free as it is in beta however they plan to be a price tier service when they do become official

# Load the variables from .env into the environment
load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Tell me more about Proxima B",
        }
    ],
    model="llama-3.1-8b-instant",
)

print(chat_completion.choices[0].message.content)
