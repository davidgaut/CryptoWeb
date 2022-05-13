'''
import requests
import urllib.request

def get_news():
    response = requests.get('https://newsapi.org/v2/everything?q=bitcoin&apiKey=8b04a9d1d8314f3bacc0241959b7ae1d')
  
    get_news_data = response.json()
          
    news_results = None
        
    if get_news_data['articles']:
        news_results_list = get_news_data['articles']
            # print(news_results_list)
        news_results = process_results(news_results_list)
           


    return news_results
        
    
def process_results(news_list):
    ''''''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    ''''''
    news_results = []
    for news_item in news_list:
        title = news_item.get('title')
        description = news_item.get('description')
        content = news_item.get('content')
        publishedAt = news_item.get('publishedAt')

        
        news_object = News(title,description,content,publishedAt)
        #print(news_object)
        news_results.append(news_object)
        # print(news_results)

    return news_results 
    
class News:
    ''''''
    News class to define News Objects
    ''''''

    def __init__(self,title,description,content,publishedAt):
        self.title = title
        self.description = description
        self.content = content
        self.publishedAt= publishedAt
class Sources:
    ''''''
    News class to define News Objects
    ''''''

    def __init__(self,name,description,url):
        self.name = name
        self.description = description
        self.url = url
            
'''

from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='8b04a9d1d8314f3bacc0241959b7ae1d')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='bitcoin')

# /v2/top-headlines/sources
sources = newsapi.get_sources()