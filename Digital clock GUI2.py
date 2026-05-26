import tkinter as tk

count = 0
#. after() can call a fnc after X milliseconds


def update():
        global count      #global is used since the variable count is defined outside the fnc

        count += 1 #increases the count by 1 second
        label.config(text = str(count))     #config updates the value , str converts the num to string since labels can only display teext not nums

        window.after(1000 , update )
# wait 1second , then call the fnc

window = tk.Tk()
window.title("Digital clock")
window.config(bg = "black")

label = tk.Label(window , text = "0" , font = ("Arial" , 40) , bg = "black" , fg = "lime" )
label.pack() #makes the LABEL APPEAR ON THE WINDOW

update()
window.mainloop()