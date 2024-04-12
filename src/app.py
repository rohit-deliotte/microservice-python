from flask import Flask,jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/status")
def status():
    return jsonify(
        Status = "Up and Running"
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')