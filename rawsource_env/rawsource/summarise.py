import requests
import time

def summarise_articles(articles):
    print "STARTING THE COLLATION:"
    summaries = ""
    for x in range(0,3):
        print "starting a summary"
        print articles[x]['content']
        r = sum(articles[x]['content'], 4)
        summaries += r.json()['sm_api_content']
        time.sleep(10)
    return sum(summaries, 4).json()['sm_api_content'].split('.')

def sum(text, sentences):
    api_key = "C58B5D32BA"
    request = requests.post('http://api.smmry.com/&SM_API_KEY=' + api_key + "&SM_LENGTH=" + str(sentences), data = {'sm_api_input': text})

    return request
