from groqAPI import loadGroqClient,groqMessageRequest
from openRouter import loadOpenRouterClient, liquidMessageRequest, llamaMessageRequest

groqClient = loadGroqClient()
openRouterClient = loadOpenRouterClient()

message = ""
while(message != "bye"):
    message = input("Ask me anything:")
    # print(llamaMessageRequest(message,openRouterClient))
    print(groqMessageRequest(message,groqClient))



