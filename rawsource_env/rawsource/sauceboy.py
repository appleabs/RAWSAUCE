from eventregistry import *
import json

def get_articles(search_term):
    er = EventRegistry(apiKey = "281f5566-f0f3-467e-b525-b145f18955df")
    q = QueryArticlesIter(keywords = search_term.split(), lang = "eng", dateStart = (datetime.datetime.today() - datetime.timedelta(days=30)))
    articles = q.execQuery(er, sortBy = "rel", maxItems = 200 ,returnInfo = ReturnInfo())
    uri_list = []
    for article in articles:
        uri_list.append({"url" : str(article['url']), "sim" : article['sim'], "content" : article['body']})

    sorted_urls =  sorted(uri_list, key = lambda art: art["sim"], reverse = True)

    if len(sorted_urls) < 10:
        return format_results(sorted_urls, len(sorted_urls))
    else:
        return format_results(sorted_urls, 10)

def format_results(sorted_list, limit):
    final_array = []

    for x in range(0, limit):
        final_array.append({"url" : sorted_list[x]['url'], "content" : sorted_list[x]['content']})

    return final_array
