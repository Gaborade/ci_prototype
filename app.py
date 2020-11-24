from flask import Flask, request, jsonify
from config import Config
from utils import start_ngrok


app = Flask(__name__)
app.config.from_object(Config)
if app.config['START_NGROK']:
    start_ngrok()



@app.route('/')
def home():
    return "<h1>Arachne's Web</h1>"
    

@app.route('/github-info', methods=['GET', 'POST'])
def github_info():
    if request.method == 'POST':
        github_data = request.get_json()
        return jsonify(github_data)



if __name__ == "__main__":
    app.run(debug=True, port=500)