import json
from tkinter import *
from tkinter import  messagebox
from random import choice,randint,shuffle
import pyperclip
BLACK = "#000000"
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
    #Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [ choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [ choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [ choice(numbers) for _ in range(randint(8, 10))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    shuffle(password_list)

    password = "".join(password_list)

    entry_password.delete(0,END)
    entry_password.insert(0,password)
    print(f"Your password is: {password}")
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    print("add")
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()
    new_data = {website : {
        "email":email,
        "password":password,
    }}

    if len(website)>0 and len(password)>0:
        is_ok = messagebox.askokcancel(title="Confirmation needed",message=f"Are You Sure that you want to save \n ")
        if is_ok:
            try:
                with open("data.json", mode="r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", mode="w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", mode="w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                entry_password.delete(0,END)
                entry_website.delete(0,END)

    elif len(website) == 0:
        messagebox.showinfo(title="Invalid entry", message="You left empty space \n in website input !")

    elif len(password) == 0:
        messagebox.showinfo(title="Invalid entry", message="You left empty space \n in password input !")

# ---------------------------- SEARCH --------------------------------- #
def search():
    print("search in saved passwords")
    website = entry_website.get()
    if len(website) >0:
        try:
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)
                print(data[website])

                password = data[website]["password"]
                email = data[website]["email"]
                print("email: " + email)
                print("password: " + password)

                entry_password.delete(0, END)
                entry_email.delete(0, END)

                entry_email.insert(0, string=email)
                entry_password.insert(0, string=password)

        except FileNotFoundError:
            print("no data was previously saved \n save some passwords first !")
            messagebox.showinfo(title="no data found", message="no data was previously saved \n save some passwords first !")
        except KeyError:
            print(f"there is no password and email saved for this {website} website")
            messagebox.showinfo(title = f"there is no data this {website} website",message=f"there is no password and email saved for this {website} website")



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=YELLOW, highlightthickness=4)

canvas = Canvas(width=200, height=200, highlightthickness=3)
logo_png = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_png)
canvas.grid(column=1, row=0)

website_label = Label(text="website", fg=BLACK, bg=YELLOW, font=(FONT_NAME, 12))
website_label.grid(column=0, row=1)

user_email_label = Label(text="user/email", fg=BLACK, bg=YELLOW, font=(FONT_NAME, 12))
user_email_label.grid(column=0, row=2)

password_label = Label(text="password", fg=BLACK, bg=YELLOW, font=(FONT_NAME, 12))
password_label.grid(column=0, row=3)

entry_website = Entry(width=34)
entry_website.focus()
print(entry_website.get())
entry_website.grid(column=1, row=1, columnspan=1)

entry_email = Entry(width=53)
entry_email.insert(0, string="example@email.com")
print(entry_email.get())
entry_email.grid(column=1, row=2, columnspan=2)

entry_password = Entry(width=33)
entry_password.insert(END, string="")
# Gets text in entry
print(entry_password.get())
entry_password.grid(column=1, row=3)


# Buttons

# calls generate_password() when pressed
generate_password_button = Button(text="Generete Password", command=generate_password, width=15)
generate_password_button.grid(column=2, row=3)

# calls add() when pressed
generate_password_button = Button(text="Add", command=save, width=45)
generate_password_button.grid(column=1, row=4, columnspan=2)

# calls search() when pressed
search_button = Button(text="Search", command=search, width=14)
search_button.grid(column=2, row=1)

window.mainloop()
