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
            "creator": "AmmarBN",
            "message": "Masukkan parameter URL"
        })
    try:
        api_response = requests.post('https://api.tikmate.app/api/lookup', data=json.dumps({'url': url}))
        api_response.raise_for_status()
        response = api_response.json()
        username = response.get('author_name', '')
        desc = response.get('desc', '')
        create_up = response.get('create_time', '')
        result_url = f"https://pride.nowmvideo.com/download/{response['token']}/{response['id']}.mp4"
        return jsonify(
            {
                "username": username,
                "description": desc,
                "created_at": create_up,
                "result": result_url
            }
        )
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Gagal terhubung dengan server Tikmate"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500
