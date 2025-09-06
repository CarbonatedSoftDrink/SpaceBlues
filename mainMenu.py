import tkinter as tk
from tkinter import *

def tutorial():
    w = tk.Tk()
    w.title('How to Play')
    w.geometry("600x400")
    w
    e = Label(w, text="I'll fill this in later", bg="lightblue")
    e.pack()
    button = tk.Button(w, text='Okay', width=25, command=w.destroy)
    button.pack()
    e.mainloop()

def mainMenu():
    r = tk.Tk()
    r.title('Space Blues')
    r.geometry("600x400")
    w = Label(r, text='Welcome to Space Blues', bg="lightblue")
    w.pack()
    button = tk.Button(r, text='Play', width=25, command=r.destroy)
    button.pack()
    button = tk.Button(r, text='How to Play', width=25, command=tutorial)
    button.pack()
    button = tk.Button(r, text='Quit', width=25, command=r.destroy)
    button.pack()
    r.mainloop()

if __name__ == "__main__":
    mainMenu()