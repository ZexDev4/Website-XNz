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
    headers = {'Host': 'api.tikmate.app','sec-ch-ua': 'Google','sec-ch-ua-platform': 'Windows','sec-ch-ua-mobile': '?0','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.111 Safari/537.36','content-type': 'multipart/form-data; boundary=----WebKitFormBoundarylQlbfSRCFqG9RvRs','accept': '*/*','origin': 'https://tikmate.app','sec-fetch-site': 'same-site','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty',}
	
    response = requests.post('https://api.tikmate.app/api/lookup', data={'url': url}).text
    return jsonify({response})
