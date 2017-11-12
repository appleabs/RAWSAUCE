from eventregistry import *
import json

search_term =  raw_input("Enter a search term: ")
er = EventRegistry(apiKey = "281f5566-f0f3-467e-b525-b145f18955df")
q = QueryArticlesIter(keywords = search_term.split(), lang = "eng", dateStart = (datetime.datetime.today() - datetime.timedelta(days=30)))
articles = q.execQuery(er, sortBy = "rel", maxItems = 200 ,returnInfo = ReturnInfo())
uri_list = []
for article in articles:
    uri_list.append({"url" : str(article['url']), "sim" : article['sim']})

sorted_urls =  sorted(uri_list, key = lambda art: art["sim"], reverse = True)

json_array = []

for x in range(0,10):
    json_array.append(sorted_urls[x])

print json.dumps(json_array)
