from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"status": 200, "message": "API Giovanna_De_Souza_Nunes"})