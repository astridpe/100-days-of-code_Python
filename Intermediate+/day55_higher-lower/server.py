from flask import Flask
import random

# Generate a random number between 0 and 9 or any range of numbers of your choice.
RANDOM_NUMBER = random.randint(0, 9)

# Create a new Flask application where the home route displays an <h1> that says
# "Guess a number between 0 and 9" and display a gif of your choice

app = Flask(__name__)


@app.route("/")
def greeting():
    return "<h1>Guess a number between 0 and 9<h1>" \
           "<img src='https://media.giphy.com/media/hvLwZ5wmarjnNKEJqq/giphy-downsized-large.gif'>"


# Create a route that can detect the number entered by the user and checks that number
# against the generated random number. If the number is too low, tell the user it's too low,
# same with too high or if they found the correct number. try to make the <h1> text a different colour for each page.
@app.route("/<int:number>")
def check_number(number):
    if number < RANDOM_NUMBER:
        return "<h1 style='color: red'>Too low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"

    elif number > RANDOM_NUMBER:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)
