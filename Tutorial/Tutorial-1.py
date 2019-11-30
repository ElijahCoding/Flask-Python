from flask import Flask

app = Flask(__name__)

@app.route("/home")
def home():
    return 'Hello, <h1>World</h1>'

if __name__ == "__main__":
    app.run()