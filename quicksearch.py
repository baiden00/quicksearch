from tkinter import*
import webbrowser
import time

window = Tk()
window.title("Search for anything on the internet")
window.geometry('350x25')


window.configure(bg='red')

input = Entry(window, width=28)
input.grid(column=1, row=0)
input.focus()

def search(event=None):
    global search_string
    webbrowser.get().open('http://www.google.com/search?q=' + input.get())

window.bind('<Return>', search)

label = Label(window, text="Enter search:", font=("Lora", 15))
label.grid(column=0, row=0)


btn = Button(window, text="Search", font=("Verdana", 10), command=search)
btn.grid(column=3, row=0)



















window.mainloop()
