
#### `scraper.py`
```python
import requests
from bs4 import BeautifulSoup

def baidu_search(query):
    url = 'https://www.baidu.com/s'
    params = {'wd': query}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    response = requests.get(url, params=params, headers=headers)
    response.encoding = 'utf-8'
    return response.text

def parse_results(html):
    soup = BeautifulSoup(html, 'html.parser')
    results = []
    
    for result in soup.find_all('div', class_='result'):
        title_tag = result.find('h3')
        if title_tag:
            title = title_tag.get_text()
            link = title_tag.find('a')['href']
            results.append({'title': title, 'link': link})
    
    return results

def main():
    query = '美白'
    html = baidu_search(query)
    results = parse_results(html)
    
    for result in results:
        print(f"Title: {result['title']}")
        print(f"Link: {result['link']}\n")

if __name__ == '__main__':
    main()
