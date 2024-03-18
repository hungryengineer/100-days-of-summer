from tkinter import *

window = Tk() #window defined
label = Label(padx= 150, pady=200, text='distance converter') #label defined
label.pack() #label.grid(row=5, column=0)

entry = Entry()
entry.focus()
entry['text'] = 'km'
entry.pack() # entry.grid(row=3, column=0)

def value():
    mi = float(entry.get())
    km=mi*1.6
    km_label.config(text=f"{km}") #most important keyword 'config'

button = Button(width=8, text='calculate')
button['command'] = value
button.pack() #button.grid

km_label =Label()
km_label.pack()

window.mainloop()