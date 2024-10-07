from groqAPI import loadGroqClient,groqMessageRequest
from openRouter import loadOpenRouterClient, liquidMessageRequest, llamaMessageRequest
from bingSearch import bingSearchRequest


#LLM Clients
groqClient = loadGroqClient()
openRouterClient = loadOpenRouterClient()

message = ""
while(message != "bye"):
    message = input("Ask me anything:")

    print(bingSearchRequest(message))
    # print(llamaMessageRequest(message,openRouterClient))
    # print(groqMessageRequest(message,groqClient))



