from flask import Flask, render_template
import requests

response = requests.get("https://api.npoint.io/1e28b176e629a3b4f155")
post_data = response.json()

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", post_data=post_data)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/post<int:num>")
def get_post(num):
    requested_post = None
    for blog_post in post_data:
        if blog_post["id"] == num:
            requested_post = blog_post

    return render_template("post.html", post=requested_post)


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
