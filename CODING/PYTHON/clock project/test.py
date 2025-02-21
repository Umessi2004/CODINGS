import tkinter as t

def create_window():
    #create the main window
    root=t.Tk()
    root.title("tkinter example")
    
    #create a label widget to display hello
    label=t.Label(root, text="hello")
    #label.pack(pady=100)
    
    #to set the geometry of the window as per required!
    root.geometry('350x200')
    
    b1=Button(root, text="enter")
    
    #start the tkinter event loop
    root.mainloop()
    
if __name__=="__main__":
    create_window()
    