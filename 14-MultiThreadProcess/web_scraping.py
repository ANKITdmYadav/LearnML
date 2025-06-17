
import bs4,threading,requests
from bs4 import BeautifulSoup

urls=[
    'https://www.langchain.com/langgraph',
    'https://www.langchain.com/resources',
    'https://www.langchain.com/langchain'
]

def fetch_content(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    print(f'fetched {len(soup.text)} characters from {url}')

threads=[]
for url in urls:
    thread=threading.Thread(target=fetch_content,args=(url,))
    threads.append(thread)
    thread.start()
for t in threads:
    t.join()
print("all pages fetched")