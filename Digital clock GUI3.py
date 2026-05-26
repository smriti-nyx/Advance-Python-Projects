from datetime import datetime
import tkinter as tk

# define the function
def update():
    time = datetime.now().strftime("%H:%M:%S")
    label.config(text = time)
    window.after(1000 , update)

#create the window
window = tk.Tk()
window.title("Digital clock")
window.config(bg = "black")

#create the label
label = tk.Label(window , text = " " , font = ("Arial" , 40 ) , bg = "black" , fg = "lime")
label.pack(padx = 40 , pady = 40 )

#start the loop
update()

window.mainloop()