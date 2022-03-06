from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

def button_clicked():
    my_label.config(text=input.get())

# Label:
my_label = Label(text="I Am a label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)

my_label["text"] = "New Text"
my_label.config(text="New Text")

# Button:
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

button2 = Button(text="Click Me", command=button_clicked)
button2.grid(column=2, row=0)

# Entry:
input = Entry(width=10)
input.grid(column=3, row=3)






window.mainloop()