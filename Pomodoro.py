from plyer import notification
import tkinter as tk

work_time = 25*60 #1500 seconds
time_left = work_time
running = False

def update ():
    if running and time_left > 0:
        mins = time_left //60
        secs = time_left %60
        label.config(text =f"{mins:02} :{secs:02}")
        window.after(1000 , update )
        time_left -= 1



    elif time_left == 0 :
        label.config(text = "00:00")
        notification.notify(
            title= "Pomodoro done",
            message = "25 mins up . Reset the timer ?",
            app_name ="Pomodoro clock",
            timeout = 6
      )



def toggle ():
  global running , time_left
  if not running:
      running = True
      btn.config(text ="Stop")
      update()
  else :
     running = False
     btn.config(text = "Start")

window = tk.Tk()
window.title("Pomodoro timer ")
window.config(bg = "black")

label = tk.Label(window , text = "25:00" ,font = ("Arial" , 40) , bg = "black", fg = "lime")
label.pack(padx = 40 , pady = 40)

btn = tk.Button(window , text = "Start", font = ("Arial" , 14) , bg = "black", fg = "lime", command = toggle)
btn.pack(pady = 10)

window.mainloop()