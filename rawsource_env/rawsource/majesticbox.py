import os
from majesticseo_external_rpc.APIService import *
from urlparse import urlparse

def doit(url_list):

    endpoint = 'https://api.majestic.com/api_command'

    article_dict = []

    parameters = {}
    for index, item in enumerate(url_list):
        parsed_uri = urlparse(item['url'])
        domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
        article_dict.append({"domain": domain, "url" : url_list[index]['url'], "content" : url_list[index]['content']})
        parameters['item' + str(index)] = domain

    parameters.update({'items': len(url_list)})

    parameters.update({'datasource' : 'fresh'})

    api_service = APIService(os.environ.get('MAJESTIC_API_KEY'), endpoint)
    response = api_service.execute_command('GetIndexItemInfo', parameters)

    if(response.is_ok()):
        unsorted_results = []

        results = response.get_table_for_name('Results')

        for row in results.rows:
            trustFlow = row['TrustFlow']
            item = row['Item']
            if trustFlow > 50:
                print item + " - trustflow: " + trustFlow
                unsorted_results.append({'domain': item, 'trustFlow' : trustFlow})

        sorted_results =  sorted(unsorted_results, key = lambda result: result["trustFlow"], reverse = True)

        print sorted_results

        top_three = []
        top_article_urls = []

        if len(sorted_results)>3:
            top_three = get_articles(3,sorted_results)
        else:
            top_three = get_articles(len(sorted_results),sorted_results)

        for trust_object in top_three:
            for x in range(0,len(url_list)):
                if trust_object['domain'] == article_dict[x]['domain']:
                    top_article_urls.append({"url" : article_dict[x]['url'], "content" : article_dict[x]['content']})

        return top_article_urls

def get_articles(limit, results):
    topthree = []
    for j in range(0, limit):
        topthree.append(results[j])
    return topthree
