from dotenv import load_dotenv
import json
import os 
from pprint import pprint
import requests

'''
This sample makes a call to the Bing Web Search API with a query and returns relevant web search.
Documentation: https://docs.microsoft.com/en-us/bing/search-apis/bing-web-search/overview
'''

# Add your Bing Search V7 subscription key and endpoint to your environment variables.

def bingSearchRequest(query):

    load_dotenv()

    subscription_key = os.getenv("BING_SEARCH_SUBSCRIPTION_KEY")
    endpoint = "https://api.bing.microsoft.com/v7.0/search"

    # Construct a request
    params = { 'q': query}
    headers = { 'Ocp-Apim-Subscription-Key': subscription_key }

    # Call the API
    try:
        response = requests.get(endpoint, headers=headers, params=params)
        response.raise_for_status()
        return extractUrls(response)

        

    except Exception as ex:
        raise ex
    

def extractUrls(queryResponse):
        search_results = queryResponse.json()
        urls = []
        if 'webPages' in search_results:
            urls = [item['url'] for item in search_results['webPages']['value']]

        return urls[:5]  #returns top 5 links