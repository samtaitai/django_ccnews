from django.shortcuts import render
import requests
import datetime

# Create your views here.

def index(request):
    url = 'https://newsapi.org/v2/everything?q=charlie+cox+daredevil&language=en&sortBy=relevancy&apiKey=ba6cda25a8c148d68f92278c1f29526b'
    my_news = requests.get(url).json()

    total_results = my_news['totalResults']
    fetched_articles = my_news['articles']
    desc = [] # empty array
    title = []
    img = []
    url = []
    date = []
    
    for i in range(len(fetched_articles)):
        fetched_article = fetched_articles[i]
        title.append(fetched_article['title']) 
        desc.append(fetched_article['description'])
        img.append(fetched_article['urlToImage'])
        url.append(fetched_article['url'])
        d1 = datetime.datetime.strptime(fetched_article['publishedAt'], "%Y-%m-%dT%H:%M:%SZ")
        new_format = "%B %d, %Y"
        date.append(d1.strftime(new_format))
        mylist = zip(title, desc, img, url, date) # assemble!
    
    context = {'mylist': mylist, 'total_results': total_results}

    return render(request, 'MainApp/index.html', context)
