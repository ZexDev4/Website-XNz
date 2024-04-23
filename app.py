from flask import Flask, request, jsonify, render_template
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

@app.route('/')
def Home_Page():
	return render_template('index.html')

@app.errorhandler(404)
def not_found_error(error):
	return jsonify({"message": "page not found"}), 404

if __name__ == '__main__':
	app.run(debug=True)
