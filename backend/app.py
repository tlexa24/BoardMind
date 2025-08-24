from flask import Flask, jsonify
from flask_cors import CORS
from config import Config
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
CORS(app)

@app.route('/')
def home():
    return "Hello, BoardMind!"

@app.route('/api/message')
def message():
    return jsonify(message="Hello from Flask!")


if __name__ == '__main__':
    app.run(debug=True)
