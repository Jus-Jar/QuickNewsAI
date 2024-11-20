from duckduckgo_search import DDGS

def newsDDG(query):
    results = DDGS().news(keywords=query, region="us-en", safesearch="off", timelimit="m", max_results=10)
    # Extract all bodies from the results 
    return results

#Test
# print(newsDDG("Trinidad and Tobago local news today"))