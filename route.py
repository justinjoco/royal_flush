from flask import Flask, render_template, jsonify
import json


app = Flask(__name__)


@app.route("/")
def render():
    return render_template("route.html")



if __name__ == "__main__":
    app.run(debug=True)
