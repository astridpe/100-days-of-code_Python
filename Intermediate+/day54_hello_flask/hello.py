from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper_method():
        string = function()
        return f"<b>{string}</b>"

    return wrapper_method


def make_emphasis(function):
    def wrapper_method():
        string = function()
        return f"<em>{string}</em>"

    return wrapper_method


def make_underlined(function):
    def wrapper_method():
        string = function()
        return f"<u>{string}</u>"

    return wrapper_method


@app.route('/')
def hello_world():
    return 'Hello, World!'


# Different routes using the app.route decorator:
@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye!"


# Creating variable paths and convertinf hte path to a specified data type
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} years old!"


if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True)
