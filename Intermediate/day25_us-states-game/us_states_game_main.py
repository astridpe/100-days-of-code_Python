import turtle
import pandas

FONT = ("Arial", 12, "normal")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Check if the answer is among the 50 States:
data = pandas.read_csv("50_states.csv")
state_list = data["state"].to_list()
score = 0


def write_state(state_name, x_cor, y_cor):
    text = turtle.Turtle()
    text.penup()
    text.hideturtle()
    text.goto(x_cor, y_cor)
    text.write(state_name, align="center", font=FONT)


guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{score}/50 States Correct",
                                    prompt="What's another state's name?").title()
    # Exit the game:
    if answer_state == "Exit":
        missing_states = [state for state in state_list if state not in guessed_states]
        data = pandas.DataFrame(missing_states)
        data.to_csv("states_to_learn.csv")
        break

    if answer_state in state_list:
        # Write correct guess onto the map
        state_data = data[data.state == answer_state]
        x = int(state_data.x)
        y = int(state_data.y)
        write_state(answer_state, x, y)

        # Record the correct guesses in a list
        guessed_states.append(answer_state)

        # Keep track of the score
        score += 1










