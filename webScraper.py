import requests
from bs4 import BeautifulSoup

def scrapeWebsite(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    try:
        print("scraping !")
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Ensure successful request
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract relevant text content (e.g., paragraphs, articles)
        paragraphs = [p.get_text() for p in soup.find_all('p')]
        content = ' '.join(paragraphs)
        content = cleanContent(content)

        return content
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return ""
    
def cleanContent(content):
    cleaned_content = content.replace("\n", "").strip()
    cleaned_content = content.replace("\t", "").strip()
    cleaned_content = content.replace("\r", "").strip()
    return cleaned_content
    
def condenseContent(urls):
    allContent = []
    for url in urls:
        content = scrapeWebsite(url)
        allContent.append(content)

    return ''.join(allContent)
