from tkinter import *

BLACK = "#000000"
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50,bg=YELLOW, highlightthickness=4)

canvas = Canvas(width=200, height=200, highlightthickness=3)
logo_png = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_png)
canvas.grid(column=1, row=0)

website_label = Label(text="website", fg=BLACK,bg=YELLOW,font=(FONT_NAME, 12))
website_label.grid(column=0, row=1)

user_email_label = Label(text="user/email", fg=BLACK,bg=YELLOW, font=(FONT_NAME, 12))
user_email_label.grid(column=0, row=2)

password_label = Label(text="password", fg=BLACK,bg=YELLOW, font=(FONT_NAME, 12))
password_label.grid(column=0, row=3)

entry_website = Entry(width=53)
entry_website.insert(END, string="Some text to begin with.")
#Gets text in entry
print(entry_website.get())
entry_website.grid(column=1,row=1,columnspan=2)

entry_email_username = Entry(width=53)
entry_email_username.insert(END, string="Some text to begin with.")
#Gets text in entry
print(entry_email_username.get())
entry_email_username.grid(column=1,row=2,columnspan=2)

entry_password = Entry(width=33)
entry_password.insert(END, string="Some text to begin with.")
#Gets text in entry
print(entry_password.get())
entry_password.grid(column=1,row=3)

def generate_password():
    print("generate_password")

#calls action() when pressed
generate_password_button = Button(text="Generete Password", command=generate_password,width=15)
generate_password_button.grid(column=2,row=3)

def add():
    print("add")

#calls action() when pressed
generate_password_button = Button(text="Add", command=add,width=45)
generate_password_button.grid(column=1,row=4,columnspan=2)



window.mainloop()
