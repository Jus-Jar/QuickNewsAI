from groqAPI import loadGroqClient
from openRouter import loadOpenRouterClient, liquidMessageRequest, llamaMessageRequest
from bingSearch import bingSearchRequest
from webScraper import condenseContent
from summarizer import summaryRequest
#LLM Clients
groqClient = loadGroqClient()
openRouterClient = loadOpenRouterClient()

summarizerClient = loadOpenRouterClient()




message = ""
while(message != "bye"):
    message = input("Ask me anything:")

    # I need an agent that takes the user prompt and convert it into the form of a search request
    urls = bingSearchRequest(message)
    content = condenseContent(urls)
    print(summaryRequest(content,summarizerClient))
    # I need an agent to take the user prompt and summary search and produce a response that answers the user's question.


    # print(llamaMessageRequest(message,openRouterClient))
    # print(groqMessageRequest(message,groqClient))



