from tkinter import *

from playground import calculate

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=600, height=300)
window.config(padx=100, pady=50)

input_box = Entry(width=10)
input_box.grid(column=1, row=0)

miles = Label(text = "Miles")
miles.grid(column=2, row=0)

km = Label(text = "Km")
km.grid(column=2, row=1)

equal_to = Label(text = "is equal to")
equal_to.grid(column=0, row=1)

def calculator():
    answer = int(input_box.get()) * 1.6
    new_text.config(text=answer)

button = Button(text = "Calculate", command=calculator)
button.grid(column=1, row=2)

new_text = Label(text= 0)
new_text.grid(column=1, row=1)





window.mainloop()