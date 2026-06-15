from flask import Flask, render_template, request, redirect, jsonify
from pymongo import MongoClient
import json

app = Flask(__name__)

# MongoDB Atlas Connection String
MONGO_URI = "YOUR_DBCONNECTION_STRING"

client = MongoClient(MONGO_URI)

# Database and Collection
db = client["studentdb"]
collection = db["students"]


# ----------------------
# Home Page
# ----------------------
@app.route("/")
def home():
    return render_template("form.html")


# ----------------------
# MongoDB Form Submission
# ----------------------
@app.route("/submit", methods=["POST"])
def submit():
    try:
        name = request.form["name"]
        email = request.form["email"]

        collection.insert_one({
            "name": name,
            "email": email
        })

        return redirect("/success")

    except Exception as e:
        return render_template(
            "form.html",
            error=str(e)
        )


# ----------------------
# Success Page
# ----------------------
@app.route("/success")
def success():
    return render_template("success.html")


# ----------------------
# JSON API Route
# ----------------------
@app.route("/api")
def get_data():
    with open("data.json", "r") as file:
        data = json.load(file)

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
