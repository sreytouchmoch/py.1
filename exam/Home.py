import tkinter as tk
#create empty window
root = tk.Tk()
#window size
root.geometry("600x600")
#set title
root.title("Draw Face ")
#.....
canvas = tk.Canvas(root)
#eyes one
canvas.create_oval(110, 70, 210, 150, fill="blue")
canvas.create_oval(70, 70, 250, 150)
#eyes two
canvas.create_oval(400, 70, 500, 150, fill="blue")
canvas.create_oval(360, 70, 540, 150)
#nose
canvas.create_oval(270, 240, 300, 200, fill="red")
#mouth
canvas.create_rectangle(100, 350, 120, 420, fill="red", outline="red")
canvas.create_rectangle(500, 370, 480, 400, fill="red", outline="red")
canvas.create_rectangle(100, 400, 500, 420, fill="red", outline="red")
canvas.pack(expand=True, fill="both")
root.mainloop()


