YELLOW = "#f7f5dd"

#---------------------------- PASSWORD GENERATOR ------------------------------- #


# insert and generate password
def insert_password():

    # Password Generator Project
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    # insert the password
    pass_entry.delete(0, END)
    pass_entry.insert(END, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    website = web_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Something is wrong", message="please enter a valid Username/password")
    else:
        agreed = messagebox.askokcancel(title=f"For {website} ",
                                        message=f"Email: {email}\n Password: {password}")
        if agreed:
            with open("saved.passwords.txt", mode="a+") as info:
                info.write(f"\n{website} | {email} | {password}")
                web_entry.delete(0, END)
                pass_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("PASSWORD GENERATOR")
window.config(padx=50, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=200, bg=YELLOW, highlightthickness=0)

# image
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

# website label
web_label = Label(text="Website: ", bg=YELLOW, highlightthickness=0)
web_label.grid(column=0, row=1)

# email
email_label = Label(text="Email/username:", bg=YELLOW, highlightthickness=0)
email_label.grid(column=0, row=2)

# password label
pass_label = Label(text="Password", bg=YELLOW, highlightthickness=0)
pass_label.grid(column=0, row=3)

# generate button
gen_button = Button(text="Generate Password", command= insert_password)
gen_button.grid(column=2, row=3)

# add button
add_button = Button(text="Add", width=31, command= save_data)
add_button.grid(column=1, row=4, columnspan=2)

# website Entry
web_entry = Entry(width=36)
web_entry.grid(column=1, row=1, columnspan=2)
web_entry.focus()

# email Entry
email_entry = Entry(width=36)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "xxx06@gmail.com")

# password entry
pass_entry = Entry(width=18, highlightthickness=0)
pass_entry.grid(column=1, row=3, columnspan=1)


window.mainloop()