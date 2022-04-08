from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_letters + password_symbols
    shuffle(password_list)
    password = "".join(password_list)
    txt_password.delete(0, END)
    txt_password.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    email = txt_email_user.get()
    website = txt_website.get()
    password = txt_password.get()

    if email != '' and website != '' and password != '':
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                              f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            text = f"{website} | {email} | {password}"
            with open(f"data.txt", mode="a") as data:
                data.write(f'{text}\n')

            txt_website.delete(0, END)
            txt_email_user.delete(0, END)
            txt_password.delete(0, END)
            txt_website.focus()
    else:
        messagebox.showinfo(title="Warning", message="There is one or more blank information, fill to proceed !")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=0, row=0, columnspan=3)

lbl_website = Label(text='Website: ')
lbl_website.grid(column=0, row=1, sticky="e", pady=3)
txt_website = Entry(width=58)
txt_website.grid(column=1, row=1, columnspan=2, sticky="w", pady=3)
txt_website.focus()

lbl_email_user = Label(text='Email/Username: ')
lbl_email_user.grid(column=0, row=2, sticky="w", pady=3)
txt_email_user = Entry(width=58)
txt_email_user.grid(column=1, row=2, columnspan=2, sticky="w", pady=3)
# txt_email_user.insert(0, "feehssm@live.com")

lbl_password = Label(text='Password: ')
lbl_password.grid(column=0, row=3, sticky="e", pady=3)
txt_password = Entry(width=33)
txt_password.grid(column=1, row=3, sticky="w", pady=3)

btn_generate = Button(text='Generate Password', width=20, command=generate_password)
btn_generate.grid(column=2, row=3)

btn_add = Button(text='Add', width=50, command=save)
btn_add.grid(column=1, row=4, columnspan=2, sticky="w", pady=3)

window.mainloop()
