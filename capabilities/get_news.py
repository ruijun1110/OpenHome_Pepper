import json
import requests
import os
os.environ['NEWS_API_KEY'] = 'pdbQT9LNuUeWKCu82bQSlhoiAZMzQkLl'

def get_news(news_section = "home"):
    url = ('https://api.nytimes.com/svc/topstories/v2/'+news_section+'.json?api-key=' + os.environ['NEWS_API_KEY']
    )
    response = requests.get(url, headers={'X-Api-Key': os.environ['NEWS_API_KEY']})
    data = response.json()
    news_results = data["results"]
    news_report = f"Latest {news_section} news from the New York Times: \n"
    count = 0
    for news in news_results:
        if count == 5:
            break
        news_report += 'Title:'+news["title"]+'\n'
        news_report += 'Abstract:'+news["abstract"]+'\n'
        count += 1
    return news_report