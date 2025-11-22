
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "AI Revenue Prompts OS™ is live!"

# Optional: Add an API route for ManyChat or OpenAI
@app.route('/api', methods=['GET'])
def api():
    return {"status": "success", "message": "API endpoint ready"}
