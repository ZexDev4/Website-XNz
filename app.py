from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world!'

@app.route('/download/tiktok', methods=["GET"])
def download_tiktok():
    url = request.args.get('url')
    if not url:
        return jsonify({
            "code": 404,
            "message": "Masukkan parameter URL"
	})
    response = requests.post('https://api.tikmate.app/api/lookup', data={'url': url}).json()
    return jsonify({response})
