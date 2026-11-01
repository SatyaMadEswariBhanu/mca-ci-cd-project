from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>MCA CI/CD Pipeline Project</h1>
    <h2>Welcome to DevOps Automation!</h2>
    <p>Application deployed successfully using Kubernetes.</p>
    """

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": "MCA CI/CD Demo"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
