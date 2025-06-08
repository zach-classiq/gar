from flask import Flask, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

VOTES_FILE = "votes.json"

def load_votes():
    try:
        with open(VOTES_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"yes": 0, "no": 0}

def save_votes(votes):
    with open(VOTES_FILE, "w") as f:
        json.dump(votes, f)

votes = load_votes()

@app.route('/votes', methods=['GET'])
def get_votes():
    return jsonify(votes)

@app.route('/vote/<choice>', methods=['POST'])
def cast_vote(choice):
    if choice in votes:
        votes[choice] += 1
        save_votes(votes)
        return jsonify(votes)
    else:
        return "Invalid choice", 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
