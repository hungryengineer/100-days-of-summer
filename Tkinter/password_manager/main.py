import tkinter
from tkinter import *
from tkinter import messagebox
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

def password_generator():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    [password_list.append(random.choice(letters)) for char in range(nr_letters)] #using list comprehension

    for char in range(nr_symbols):
      password_list += random.choice(symbols)


    for char in range(nr_numbers):
      password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
      password += char
    pwd_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # with open("record.txt", "a") as data:
    dict_for_json_entry = { #creating an entry in dictionary format to be loaded into the json file
        website_entry.get(): {
          "email": user_entry.get(),
          "pwd": pwd_entry.get(),
    }
}
    # with open("record.json", 'w') as data:
    if len(website_entry.get()) == 0:
            messagebox.showinfo(title='notification', message='no data recorded!')
    elif len(website_entry.get()) > 0:
            # data.write(f"{website_entry.get()} | {user_entry.get()} | {pwd_entry.get()}\n") #file style
            # json.dump(dict_for_json_entry, data, indent=3) #json style
            try:
                with open("record1.json", 'r') as data: #i) open the json file
                    data = json.load(data) # ii) read present data from the json file and store it in a variable
            except FileNotFoundError:
                print("the file doesn't exist. creating it!.")
                with open("record1.json", 'w') as data:
                  json.dump(dict_for_json_entry, data, indent=3)
            else:
                data.update(dict_for_json_entry) # iii) update the new data/entered data to json file

                with open("record1.json", 'w') as data_file: # open the json file again in write mode but this time under a new variable name
                    json.dump(data, data_file, indent=3)  # write the new data to json file

            # website_entry.delete(0, END) #to flush the current entry record
            # pwd_entry.delete(0, END)
            messagebox.showinfo(title='notification', message='data saved successfully!')

#-------------------------------find password--------------------------#

def find_password():
    website = website_entry.get()
    with open ("record1.json") as data_file:
        data = json.load(data_file)
        if website in data:
          email = data[website]["email"]
          pwd = data[website]["pwd"]
          try:
            messagebox.showinfo(title='notification', message=f'data already exists! \n email: {email} \n password: {pwd}')
          except FileNotFoundError:
              messagebox.showerror(title='error', message='uhoh!')
        else:
          messagebox.showerror(title='error', message='uhoh! data does not exist')


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title(string="First Pass")
window.config(bg="#f7f5dd")

canvas = Canvas(height=200, width=225, bg="#f7f5dd")
img = PhotoImage(file="logo.png")
canvas.create_image(150,150, image=img)
canvas.grid(row=25, column=25)

#3 labels, 3 entries, 3 buttons

website_label = Label(text="website", bg="blue", font="bold", width=8, height=1)
website_label.grid(row=2, column=14, columnspan=2)

website_entry = Entry()
# website_entry.after(20,)
website_entry.grid(row=3, column=14, columnspan=4)



user_label = Label(text="email/username", bg="blue", font="bold", width=13, height=1)
user_label.grid(row=5, column=14, columnspan=3)

user_entry = Entry()
user_entry.grid(row=6, column=14, columnspan=4)



pwd_label = Label(text="password", bg="blue", font="bold", width=10, height=1)
pwd_label.grid(row=8, column=14, columnspan=2)

pwd_entry = Entry()
pwd_entry.grid(row=9, column=14, columnspan=4)

gen_pwd_button = Button(text="Generate",font="bold", command=password_generator)
gen_pwd_button.grid(row=9, column=16, columnspan=4)

add_pwd_button = Button(text="Add",font="bold", command=save)
add_pwd_button.grid(row=10, column=14, columnspan=4)

search_button = Button(text="search",font="bold", command=find_password)
search_button.grid(row=2, column=20, columnspan=5)

window.mainloop()