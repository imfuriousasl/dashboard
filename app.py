from flask import Flask, render_template
import json
import os

app = Flask(__name__, template_folder=".", static_folder=".")

DATA_FILE = "dashboard_data.json"

# Create the file if it doesn't exist
if not os.path.exists(DATA_FILE):
    default_data = {
        "births": 0,
        "antenatal": 0,
        "immunizations": 0,
        "home_visits": 0,
        "c_sections": 0
    }

    with open(DATA_FILE, "w") as f:
        json.dump(default_data, f, indent=4)


def load_data():
    with open(DATA_FILE, "r") as f:
        return json.load(f)


@app.route("/")
def dashboard():
    data = load_data()
    return render_template("dashboard.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)