from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>🚀 PLUTONET AI IS LIVE!</h1><p>Status: ONLINE ✅</p><p>Your AI Platform is running!</p>"

@app.route('/health')
def health():
    return jsonify({"status": "online", "service": "plutonet-ai"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
