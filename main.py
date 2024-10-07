from groqAPI import loadGroqClient,groqMessageRequest


groqClient = loadGroqClient()


message = ""
while(message != "bye"):
    message = input("Ask me anything:")
    print(groqMessageRequest(message,groqClient))



