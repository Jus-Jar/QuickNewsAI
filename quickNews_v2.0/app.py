from IPython.display import display, Markdown, Latex
# LangChain Dependencies
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from langchain_community.chat_models import ChatOllama
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
from langgraph.graph import END, StateGraph
# For State Graph 
from typing_extensions import TypedDict
import os
import gradio as gr
import json


from llm_client import loadLlamaLLM
from prompts import generate_agent_prompt,router_agent_prompt,query_agent_prompt
from webScraper import newsDDG

# Graph State
class GraphState(TypedDict):
    question : str
    generation : str
    search_query : str
    context : str

# Node - Generate

llm = loadLlamaLLM()
generate_prompt = generate_agent_prompt()
generate_chain = generate_prompt | llm | StrOutputParser()

router_llm= loadLlamaLLM()
router_prompt = router_agent_prompt()
question_router = router_prompt | router_llm | StrOutputParser()

query_llm = loadLlamaLLM()
query_prompt = query_agent_prompt()
query_chain = query_prompt | query_llm | JsonOutputParser()



def generate(state):
    """
    Generate answer

    Args:
        state (dict): The current graph state

    Returns:
        state (dict): New key added to state, generation, that contains LLM generation
    """
    print(state)
    print("Step: Generating Final Response")
    question = state["question"]
    context = state["context"] if state.get("context") else ""

    # Answer Generation
    generation = generate_chain.invoke({"context": context, "question": question})
    return {"generation": generation}

# Node - Query Transformation


def transform_query(state):
    """
    Transform user question to web search

    Args:
        state (dict): The current graph state

    Returns:
        state (dict): Appended search query
    """
    
    print("Step: Optimizing Query for Web Search")
    question = state['question']
    gen_query = query_chain.invoke({"question": question})
    search_query = gen_query["query"]
    return {"search_query": search_query}


# Node - Web Search

def web_search(state):
   
    search_query = state['search_query']
    print(f'Step: Searching the Web for: "{search_query}"')
    # Web search tool call
    search_result = newsDDG(search_query)
    print(search_result)
    return {"context": search_result}


# Conditional Edge, Routing

def route_question(state):
    """
    route question to web search or generation.

    Args:
        state (dict): The current graph state

    Returns:
        str: Next node to call
    """

    print("Step: Routing Query")
    question = state['question']
    output = question_router.invoke({"question": question})
    output = json.loads(output) if isinstance(output, str) else output
    print(output)
    if output['choice'] == "web_search":
        print("Step: Routing Query to Web Search")
        return "websearch"
    elif output['choice'] == 'generate':
        print("Step: Routing Query to Generation")
        return "generate"
    

workflow = StateGraph(GraphState)
workflow.add_node("websearch", web_search)
workflow.add_node("transform_query", transform_query)
workflow.add_node("generate", generate)

# Build the edges
workflow.set_conditional_entry_point(
    route_question,
    {
        "websearch": "transform_query",
        "generate": "generate",
    },
)
workflow.add_edge("transform_query", "websearch")
workflow.add_edge("websearch", "generate")
workflow.add_edge("generate", END)

# Compile the workflow
local_agent = workflow.compile()

def run_agent(query,history):
    output = local_agent.invoke({"question": query})
    # print(output["generation"])
    return {"role": "assistant", "content": output["generation"]}

gr.ChatInterface(run_agent, type="messages", title="QuickNews AI").launch()

