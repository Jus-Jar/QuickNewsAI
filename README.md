# QuickNewsAI

## Key Idea:
What this MultiAgent AI should do is act as a chat bot where the user can ask questions about particular events, trends and news and issues a summarized respose with enough content where the user can encapsulate key information surrounding the topic. 
This way users can easily stay up to date with topics without spending the time to read articles or research.

## Design
* We plan to use a Multiagent AI approach where we would use a Search API to pool together relevant articles based on the question asked by the user.
* The articles retrieved would be fed into an LLM model to process the content and essentially filter out  the relevant information
* Another LLM would be used to present the information in a simplistic format in which the user can easily process.
* In addition to this a chat interface frontend must be created for the user to interact with QuickNews AI
