from flask import Flask, render_template, jsonify
import json


app = Flask(__name__)


@app.route("/")
def render():
    return render_template("route.html")

@app.route("/locations")
def location_data():

    with open('locations.json') as file:
        json_data = json.load(file)
    return jsonify(json_data["locs"])

if __name__ == "__main__":
    app.run(debug=True)
