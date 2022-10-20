import tkinter as tk
root = tk.Tk()

#specify title and size of the root window
root.title("A label Inside a Root Window")
root.geometry("800x200")

#Create a label inside the root window
label = tk.Label(text="this is a label", fg="Red", font=("Helvetica, 80"))
label.pack() #specify where to put the label
#run the main loop
root.mainloop()

