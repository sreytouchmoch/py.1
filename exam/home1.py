import tkinter as tk
import random
from random import randrange
# Create an empty window
root = tk.Tk()
# Set TK window size to width 600 px and height 200 px
root.geometry("550x200")
canvas = tk.Canvas(root)

# Your code
randomNumber=randrange(0,10)
for index in range(0,10):
    if index==randomNumber:
        canvas.create_oval(index*50,50,50+(index*50),100, fill="green")
    else:
        canvas.create_oval(index*50,50,50+(index*50),100, fill="pink")
# pack means "draw what i put inside"
canvas.pack(expand=True, fill='both')

# Display all
root.mainloop()
