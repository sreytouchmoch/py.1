import tkinter as tk
import random
# Create an empty window
root = tk.Tk()
# Set TK window size to width 600 px and height 200 px
root.geometry("550x200")
canvas = tk.Canvas(root)
for index in range(0,6):
    for k in range(0,6):
        x1=10+(colum*50)
        y1=10+(row*50)
        x2=x1+50
        y2=y1+50
        if row ==column:
            color="blue"
        else:
            color="yellow"


        canvas.create_oval( fill="pink")
# pack means "draw what i put inside"
canvas.pack(expand=True, fill='both')

# Display all
root.mainloop()
