from tkinter import *

from playground import calculate

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=600, height=300)
window.config(padx=100, pady=50)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = Label(text ="Miles")
miles_label.grid(column=2, row=0)

kilometer_label = Label(text ="Km")
kilometer_label.grid(column=2, row=1)

is_equal_to = Label(text ="is equal to")
is_equal_to.grid(column=0, row=1)

def calculator():
    answer = int(miles_input.get()) * 1.6
    new_text.config(text=answer)

calculate_button = Button(text ="Calculate", command=calculator)
calculate_button.grid(column=1, row=2)

new_text = Label(text= 0)
new_text.grid(column=1, row=1)





window.mainloop()