from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SEARCH PASSWORD ------------------------------- #

def search_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
            "email": email,
            "password": password,
        }
    }


    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except (FileNotFoundError, json.JSONDecodeError) :
            data={}
            #update old data with new entry
        data.update(new_data)

        with open("data.json", "w") as data_file:
                # Saving updating data
                json.dump(data, data_file, indent=4)

        website_entry.delete(0, END)
        password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Grid configuration
window.grid_columnconfigure(1, weight=1)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1, sticky="w")
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2, sticky="w")
password_label = Label(text="Password:")
password_label.grid(column=0, row=3, sticky="w")

# Entries
website_entry = Entry()
website_entry.grid(column=1, row=1, sticky="ew", padx=5, pady=2)
website_entry.focus()

email_entry = Entry()
email_entry.grid(column=1, row=2, columnspan=2, sticky="ew", padx=5, pady=2)
email_entry.insert(0, "ashanvimodh241@gmail.com")

# Password Frame
password_frame = Frame(window)
password_frame.grid(column=1, row=3, columnspan=2, sticky="ew", padx=5, pady=2)

password_entry = Entry(password_frame)
password_entry.pack(side="left", fill="x", expand=True)

generate_password_button = Button(password_frame, text="Generate Password", width=15, command=generate_password)
generate_password_button.pack(side="right", padx=5)

# Buttons
search_button = Button(text="Search", width=15, command=search_password)
search_button.grid(column=2, row=1, sticky="ew", padx=5, pady=2)

add_button = Button(text="Add", command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="ew", padx=5, pady=2)

window.mainloop()