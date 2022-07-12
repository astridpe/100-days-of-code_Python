from flask import Flask, render_template, request
import requests
import smtplib

MY_EMAIL = ""
PASSWORD = ""

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


# day60 implementing html-forms:
@app.route("/contact", methods=["GET", "POST"])
def receive_data():
    if request.method == "POST":
        data = request.form
        mail = f"Name: {data['name']} \n" \
               f"Email: {data['email']} \n" \
               f"Phone: {data['phone']} \n" \
               f"Message: {data['message']} \n"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg=f"Subject:New Message\n\n {mail}"
                                )

        message = "Successfully sent your message"
        message_sent = True
        return render_template("contact.html", message=message, message_sent=message_sent)
    else:
        return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
