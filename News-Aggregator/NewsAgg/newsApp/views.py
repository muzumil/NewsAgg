from django.shortcuts import render
from newsapi import NewsApiClient
# Create your views here.

def index(request):
    newsApi = NewsApiClient(api_key = 'a5b8dcb4b6804a8c912d3404c989f854')
    headLines = newsApi.get_top_headlines(country = 'in',category = 'business')
    articles = headLines['articles']
    desc = []
    news = []
    img = []
    url = []
    
    for i in range(len(articles)):
        article = articles[i]
        desc.append(article['description'])
        news.append(article['title'])
        img.append(article['urlToImage'])
        url.append(article['url'])
    
    mylist = zip(news, desc, img, url)
    
    return render(request, 'main/index.html', context={'mylist' : mylist})