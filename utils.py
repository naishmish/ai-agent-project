import requests
import os

def search_web(query):
    search_api_url = f'https://serpapi.com/search?q={query}&api_key={os.getenv("SERPAPIKEY")}'
    response = requests.get(search_api_url)
    return response.json()

def extract_information(query, search_results):
    groq_api_key = os.getenv("groq")
    url = "https://api.groq.com/v1/query"

    headers = {
        'Authorization': f'Bearer {groq_api_key}',
        'Content-Type': 'application/json',
    }

    payload = {
        "query": query,
        "search_results": search_results.get('organic_results', [{}])[0].get('snippet', 'No snippet found')
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        result = response.json()
        return result.get('extracted_data', 'No data found')
    else:
        return f"Error: {response.status_code} - {response.text}"
