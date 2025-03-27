from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Render! Your Flask app is running successfully. A quick change to test."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
