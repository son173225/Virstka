from flask import Flask, Response, jsonify,json
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.get("/")
def index():
    return "Hello world"
@app.get("/api/us")
def get_us():
    us = [
        {
            "name": "Типо Йоу",
            "description": "Типо Йоу!",
            "date": "2025-03-26"
        }
    ]
    return Response(json.dumps(us), content_type="application/json") 
def main():
    app.run("localhost", 8010, True)

if __name__ == "__main__":
    main()