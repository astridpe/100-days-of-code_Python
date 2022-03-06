from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=280, height=50)
window.config(padx=30, pady=30)


def button_clicked():
    miles = float(entry.get())
    km = round(miles * 1.609344)
    result.config(text=f"{km}")


# Labels:
equal_to = Label(text="is equal to")
equal_to.grid(column=0, row=1)

result = Label(text=0)
result.grid(column=1, row=1)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# Button:
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

# Entry
entry = Entry(width=8)
entry.grid(column=1, row=0)
entry.insert(END, string="0")

window.mainloop()
