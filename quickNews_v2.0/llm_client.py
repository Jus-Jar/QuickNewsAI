import os
from typing import Optional
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from prompts import generate_agent_prompt, router_agent_prompt
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser

# Load the variables from .env into the environment
load_dotenv()

class ChatOpenRouter(ChatOpenAI):
    openai_api_base: str
    openai_api_key: str
    model_name: str

    def __init__(self,
                 model_name: str,
                 openai_api_key: Optional[str] = None,
                 openai_api_base: str = "https://openrouter.ai/api/v1",
                 **kwargs):
        openai_api_key = openai_api_key or os.getenv('OPENROUTER_API_KEY')
        super().__init__(openai_api_base=openai_api_base,
                         openai_api_key=openai_api_key,
                         model_name=model_name, **kwargs)
        
    

def loadLlamaLLM():
    llm = ChatOpenRouter(
        model_name="meta-llama/llama-3.2-3b-instruct:free"
    )
    return llm


llm = loadLlamaLLM()
