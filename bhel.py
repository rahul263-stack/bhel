from flask import Flask, jsonify 

app = Flask (__name__)
@app.route("/")

def hello():
    return "hello"


@app.route("/bfhl")

def hello2():
    return 

if __name__ == "__main__":
    app.run()