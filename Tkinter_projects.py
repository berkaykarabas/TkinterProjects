import tkinter

window = tkinter.Tk()
window.title("Pythob Tkinter")
window.minsize(width=450,height=350)
def button_click():
    user_input=my_entry.get()
    print(user_input)
#label
my_label = tkinter.Label(text="This is a label",font=('Arial',30,'italic'))
#my_label.config(bg="black",fg="white")
my_label.pack()

#button
my_button=tkinter.Button(text="This is a button",command=button_click)
my_button.pack()

#entry
my_entry=tkinter.Entry(width=20)
my_entry.pack()
window.mainloop()