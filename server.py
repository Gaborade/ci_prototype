from flask import Flask, request, Response
from config import Config
from utils import start_ngrok
import json


app = Flask(__name__)
app.secret_key = app.config['SECRET_KEY']
app.config.from_object(Config)
if app.config['START_NGROK']:
    start_ngrok()



@app.route('/')
def home():
    return "<h1>Arachne's Web</h1>"
    

@app.route('/github-webhook', methods=['POST'])
def github_webhook():
    print('Json here:', request.json)
    return 'ok'


    """if request.headers['Content-Type'] == 'application/json':
        if request.method == 'POST':
            github_data = request.get_json()
            return jsonify(github_data)"""



if __name__ == "__main__":
    app.run(debug=True, port=5000)
    