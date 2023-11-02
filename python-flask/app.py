from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome to flask! \n"

@app.route("/hello")
def hello():
    return "Hello, this is a response from flask! \n"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)