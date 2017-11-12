from flask import Flask, request, render_template, url_for, redirect
from sauceboy import get_articles
from majesticbox import doit
from summarise import summarise_articles
import time

#from neutralitySorter import emotionRank
app = Flask(__name__, template_folder='templates')

@app.route("/")
@app.route("/hello")
def hello():
    return render_template('ijeoma.html')

@app.route("/searchforasummary", methods=['GET', 'POST'])
def testing():
    global_start_time = time.clock()
    print "########"
    print "STARTING"
    print "#######"

    #Get user's entered search term
    search_term = request.args.get("searchterm")

    #Get list of most related articles in the last 30 days with EventRegistry API
    time_start = time.clock()
    articles_list = get_articles(search_term)
    print "Getting the relevant article data took " + str((time.clock() - time_start)) + " seconds"

    #Get the three most trusted articles from the list with Majestic API
    time_start = time.clock()
    trusted_articles_list = doit(articles_list)
    print "Getting the three most trusted articles from the list with the Majestic API took " + str((time.clock() - time_start)) + " seconds"

    #Get the article with the most 'neutrality' with the IBM API (deprecated)
    #neutralised_list = []
    #for url in articles_list:
    #    neutralised_list.append(emotionRank(url))

    summaries = summarise_articles(trusted_articles_list)
    del summaries[len(summaries)-1]

    print "######"
    print "Total time taken: " + str((time.clock() - global_start_time)) + " seconds"
    print "######"
    print "last point: " + summaries[len(summaries)-1]

    #Render the page
    return render_template("summary.html", searchterm = search_term, summary = summaries)
