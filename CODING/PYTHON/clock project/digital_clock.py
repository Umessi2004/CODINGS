from tkinter import *
from datetime import *

window=Tk()
window.title("digital clock")
def update_time():
    date_time=datetime.now().strftime("%H:%M:%S")
    window.after(1000,update_time)
    time_label.config(text=f"{date_time}", font='Arial, 35', fg='red')

time_label=Label(window, text="")
time_label.pack()

update_time()
#label=Label(window, text="DIGITAL clock", font='Arial')
#label.pack()
window.mainloop()
