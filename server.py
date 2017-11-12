from flask import Flask, request, render_template, url_for, redirect
app = Flask(__name__, template_folder='templates')

@app.route("/")
@app.route("/hello")
def hello():
    return render_template('ijeoma.html')

@app.route("/searchforasummary", methods=['GET', 'POST'])
def testing():
    return render_template("summary.html", searchterm=request.args.get("searchterm"), key_points="Shit got fucked")
