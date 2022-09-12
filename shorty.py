from tkinter import *
import pyshorteners

root = Tk()
root.title("Arnav's Link Shortener")
root.geometry("500x500")

def shorten():
    if shorty.get():
        shorty.delete(0, END)
    if myEntry.get():
        url = pyshorteners.Shortener().tinyurl.short(myEntry.get())
        shorty.insert(0, url)

myLabel = Label(root, text="Enter Link To Shorten", font=("Helvetica", 34))
myLabel.pack(pady=20)

myEntry = Entry(root, font=("Helvetica", 24))
myEntry.pack(pady=20)

myButton = Button(root, text="Shorten Link", command=shorten, font=("Helvetica", 24))
myButton.pack(pady=20)

shortyLabel = Label(root, text="Shortened Link", font=("Helvetica", 14))
shortyLabel.pack(pady=50)

shorty = Entry(root, font=("Helvetica", 22), justify=CENTER, width=30, bd=0, bg="systembuttonface")
shorty.pack(pady=10)

root.mainloop()