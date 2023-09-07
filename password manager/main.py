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
from tkinter import messagebox
import json

def save_data():
    website = web_entry.get()
    email = email_entry.get()
    password = pass_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Something is wrong", message="please enter a valid Username/password")
    else:
        try:
            with open("saved.passwords.json", mode="r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("saved.passwords.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
                print("Error occured!")
        else:
            with open("saved.passwords.json", mode="w") as data_file:
                data.update(new_data)
                json.dump(data, data_file, indent=4)
                print("error didnt occur!")
        finally:
            web_entry.delete(0, END)
            pass_entry.delete(0, END)
# --------------------------- SEARCH PASSWORD --------------------------#


def find_password():
    website = web_entry.get()
    try:
        with open("saved.passwords.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error!", message="Nothing Found!")
        print("EROR")
    else:
        try:
            email = data[website]["email"]
            password = data[website]["password"]
        except KeyError:
            messagebox.showerror(title=f"{website}", message="Nothing related to this website!")
        else:
            agreed = messagebox.askokcancel(title=f"For {website} ",
                                            message=f"Email: {email}\n Password: {password}")
            if agreed:
                pass_entry.insert(0, password)
                email_entry.delete(0, END)
                email_entry.insert(0, email)



# ---------------------------- UI SETUP ------------------------------- #


from tkinter import *

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

# search button
search_button = Button(text="Search", command=find_password, width=12)
search_button.grid(column=2, row=1)

# website Entry
web_entry = Entry(width=18)
web_entry.grid(column=1, row=1)
web_entry.focus()

# email Entry
email_entry = Entry(width=36)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "xxx06@gmail.com")

# password entry
pass_entry = Entry(width=18)
pass_entry.grid(column=1, row=3, columnspan=1)


window.mainloop()