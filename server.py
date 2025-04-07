from flask import Flask, Response, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.get("/api/us")
def get_us():
    us = [
        {
            "name": "Типо Йоу",
            "description": "Типо Йоу!",
            "date": "2025-03-26"
        }
    ]
def main():
    app.run("0.0.0.0", 8010, True)

