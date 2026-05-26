print("hello world")
import tkinter as tk



window = tk.Tk()
window.title("My first window")

#adding a label : a sticky note for the window I created above
label = tk.Label(window , text = "Hello!" , font = ("Arial" , 40) , bg = "black" ,fg = "lime")
label.pack()

window.mainloop()

