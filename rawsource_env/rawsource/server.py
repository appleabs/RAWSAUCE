from flask import Flask, request, render_template, url_for, redirect
from sauceboy import get_articles
app = Flask(__name__, template_folder='templates')

@app.route("/")
@app.route("/hello")
def hello():
    return render_template('ijeoma.html')

@app.route("/searchforasummary", methods=['GET', 'POST'])
def testing():
    search_term = request.args.get("searchterm")
    articles_list = get_articles(search_term)
    return render_template("summary.html", searchterm = search_term, key_points = articles_list)
