from groqAPI import loadGroqClient
from openRouter import loadOpenRouterClient, liquidMessageRequest, llamaMessageRequest, searchInputAgentRequest,responseAgentRequest
from bingSearch import bingSearchRequest
from webScraper import condenseContent
from summarizer import summaryRequest

#LLM Clients
groqClient = loadGroqClient()
openRouterClient = loadOpenRouterClient()
summarizerClient = loadOpenRouterClient()
searchInputClient = loadOpenRouterClient()
responseClient = loadOpenRouterClient()

message = ""
while(message != "bye"):
    message = input("Ask me anything:")

    webSearchQuery = searchInputAgentRequest(message,searchInputClient)
    print(webSearchQuery)
    urls = bingSearchRequest(webSearchQuery)
    content = condenseContent(urls)
    summary = summaryRequest(content,summarizerClient)
    print(responseAgentRequest(message,summary,responseClient))
    # I need an agent to take the user prompt and summary search and produce a response that answers the user's question.


    # print(llamaMessageRequest(message,openRouterClient))
    # print(groqMessageRequest(message,groqClient))



