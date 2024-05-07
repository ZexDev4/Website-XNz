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
	url_down = (f"https://pride.nowmvideo.com/download/{response['token']}/{response['id']}.mp4")
	judul_desc = response['desc']
	tanggal_up = response['create_time']
	total_like = response['like_count']
	total_share = response['share_count']
	total_comen = response['comment_count']
	nama_tt = response['author_name']
	username_tt = response['author_id']
	return jsonify({"nama": nama_tt, "username": username_tt, "desc": judul_desc, "tanggal_upload": tanggal_up, "total_like": total_like, "total_komen": total_comen, "total_share": total_share, "url_down": url_down})
