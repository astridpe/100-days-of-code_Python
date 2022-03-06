from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
current_card = {}
word_dict = {}

# ---------------------------- GENERATE NEXT CARD ------------------------------- #

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    word_dict = original_data.to_dict(orient="records")
else:
    word_dict = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(word_dict)
    random_word = current_card["French"]
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=random_word, fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


# ----------------------------  FLIP CARDS ------------------------------- #

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


# ---------------------------- SAVE YOUR PROGRESS ------------------------------- #

def is_known():
    word_dict.remove(current_card)
    next_card()
    data_file = pandas.DataFrame(word_dict)
    data_file.to_csv("./data/words_to_learn.csv", index=False)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, fill="black", font=(FONT_NAME, 40, "italic"))
card_word = canvas.create_text(400, 263, fill="black", font=(FONT_NAME, 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons:
right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=is_known)
right_button.grid(column=1, row=1)
wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(column=0, row=1)

next_card()
window.mainloop()
