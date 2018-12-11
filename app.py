import json

from flask import Flask, request

from classifier import bias
from vectorize import model

app = Flask(__name__)

@app.route('/')
def mainPage():
    """main page of Flask application"""

    return 'Flask server for political bias detector'

@app.route('/classify',methods = ['POST'])
def classify():
    """Handle POST requests from Chrome extension"""

    if request.method == 'POST':
        articleUrl = request.get_json()['url']
        return json.dumps(bias(articleUrl,model))
      
if __name__ == '__main__':
    app.run(debug=False, port=5000)
