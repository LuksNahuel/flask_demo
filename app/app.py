from dotenv import load_dotenv
from flask import Flask, request, jsonify
from ia import IA

load_dotenv()

app = Flask(__name__)
ia = IA()

@app.route("/")
def index():
    return 'Hello World!'

@app.post("/complete")
def complete():
    prompt = request.json['prompt']
    response = ia.complete(prompt)
    return jsonify(
        {
            'response': response
        }
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
