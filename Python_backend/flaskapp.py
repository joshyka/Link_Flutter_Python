from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)


@app.route('/', methods=['GET'])
def index():
    return jsonify({'greetings': 'Hi! this is python'})


if __name__ == "__main__":
    app.run(debug=True)
