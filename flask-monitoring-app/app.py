from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask Monitoring App is Running."

@app.route("/health")
def health_check():
    return jsonify(status="healthy", message="The app is running smoothly.")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)