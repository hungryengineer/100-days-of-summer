import tkinter

window = tkinter.Tk()
window.title("GUI screen")
window.minsize(width=300, height=200)
window_label = tkinter.Label(text="Label")
window_label.grid(row=0, column=0)  #window_label.pack()

#label
window_label['text'] = 'new label'
def on_click():
    window_label['text'] = 'clicked'
    button['text'] = 'entry'

#button
button = tkinter.Button(text='button')
button.grid(row=1, column=0)   #button.pack()
button['text'] = 'new-button'
button['command'] = on_click

#entry
entry = tkinter.Entry()
entry.insert(index=0, string="starting text")
print(entry.get())
entry.grid(row=3, column=2)  #entry.pack()

#textbox

text = tkinter.Text(height=3, width=5)
text.focus() #to make the cursor start out inside the textbox
text.insert(index='1.0',chars="starting text")
print(text.get('1.0'))
text.grid(row=5, column=4)  #text.pack()

#spinbox
def used():
    print(spinbox.get())
spinbox = tkinter.Spinbox(from_=0, to=5, width=3)
spinbox['command'] = used
spinbox.grid(row=1, column=3)  #spinbox.pack()

#scale
def value(value):
    print(value)
scale = tkinter.Spinbox(from_=0, to=25, command=value)
scale.grid(row=1, column=4)  #scale.pack()

#checkbutton
def checkbutton_used():
    print(checked_state.get())
checked_state = tkinter.IntVar()
checkbutton = tkinter.Checkbutton(text="Is on?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.grid(row=1, column=6)  # checkbutton.pack()

#radiobutton

def radio_used():
    print(radio_state.get())
radio_state = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton(text='Option1', value=1, variable=radio_state)
radiobutton2 = tkinter.Radiobutton(text='Option2', value=2, variable=radio_state)
radiobutton1.grid(row=3, column=3)  # radiobutton1.pack()
radiobutton2.grid(row=3, column=0)  # radiobutton2.pack()

#listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))
listbox = tkinter.Listbox(height=4)
fruits = ["apple", "oranges", "grapes", "pears"]
for fruit in fruits:
    listbox.insert(fruits.index(fruit), fruit)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.grid(row=2, column=5)  # listbox.pack()


window.mainloop()