from flask import Flask, render_template
import datetime
import requests

app = Flask(__name__)


@app.route("/")
def home():
    current_year = datetime.datetime.now().year
    return render_template("index.html", year=current_year)


@app.route("/guess/<name>")
def guess(name):
    gender_response = requests.get(f"https://api.genderize.io?name={name}")
    gender_response.raise_for_status()
    gender_data = gender_response.json()["gender"]
    print(gender_data)

    age_response = requests.get(f"https://api.agify.io?name={name}")
    age_response.raise_for_status()
    age_data = age_response.json()["age"]
    print(age_data)

    return render_template("guess.html", name=name, gender=gender_data, age=age_data)


@app.route("/blog")
def get_blog_posts():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_post = response.json()
    return render_template("test.html", posts=all_post)


if __name__ == "__main__":
    app.run(debug=True)
