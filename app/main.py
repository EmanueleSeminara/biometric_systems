from flask import Flask

app = Flask(__nam__)

@app.route("/")
def home_view():
    return "<h1>Wlcome to Geeks for Geeks</h1>"