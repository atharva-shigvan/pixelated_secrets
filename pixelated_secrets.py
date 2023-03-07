import tkinter as tk
import os

root = tk.Tk()
root.title("Pixelated Secrets")
root.geometry("250x200")

def open_image():
    os.system('python dependancies/image.py')

def open_video():
    os.system('python dependancies/video.py')

button_a = tk.Button(root, text="Encrypt in image", command=open_image)
button_a.grid(row=0, column=0, padx=60, pady=(50,0))

button_b = tk.Button(root, text="Encrypt in video", command=open_video)
button_b.grid(row=1, column=0, padx=60, pady=(0,50))

root.mainloop()

