import sys, os
from flask import Flask, render_template, request
import requests
import json
from dotenv import load_dotenv
sys.path.append("../")
from gif_test import frame_brightness_test

load_dotenv()
TENOR_API_KEY = os.getenv("TENOR_API_KEY")
defaultQ = "exciting" # Default GIF search
lmt = 10 # GIF Limit

app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
    """Render index with query response from GIF API if query string contains a response from request.args.get('search').
    If no search query, pass 'defaultQ' to the API for a default response."""
    q = request.args.get('search')
    if not q:
        q = defaultQ
    r = requests.get(
        "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (q, TENOR_API_KEY, lmt))

    if r.status_code == 200:
        gifs = json.loads(r.content)
        gifs = gifs["results"]
        gif_tuples = list()
        title = q + " GIFs | Graphics Interchange Format Search" #Dynamic title
        for gif in gifs:
            e = frame_brightness_test(gif['media'][0]['gif']['url'])
            gif_tuple = (e, gif)
            gif_tuples.append(gif_tuple)
        return render_template(
            'index.html',
            gifs=gif_tuples,
            title=title
            )
    else:
        return "Request error code: " + r.status_code #If error status from API

if __name__ == '__main__':
    app.run(debug=True)
