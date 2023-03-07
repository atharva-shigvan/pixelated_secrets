from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image

def open_image():
    global img_path
    img_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image Files", "*.jpg *.png *.jpeg *.tif *.gif")])

def save_image():
    global secret_entry, img_path
    if secret_entry.get() == '':
        messagebox.showwarning("Warning", "Secret message cannot be empty.")
        return
    if img_path is None:
        messagebox.showwarning("Warning", "Please select an image.")
        return
    img = Image.open(img_path)
    pixel = img.load()

    message = secret_entry.get()
    message_bits = ''.join(format(ord(c), '08b') for c in message) + '11111111'

    idx = 0
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixel[i, j]
            if idx < len(message_bits):
                pixel[i, j] = (r & 0xfe | int(message_bits[idx]), g, b)
                idx += 1

    save_path = filedialog.asksaveasfilename(defaultextension=".png")
    img.save(save_path)
    messagebox.showinfo("Done", "Image saved with encrypted message.")

# Create GUI window
root = Tk()
root.title("Steganography Program")
root.geometry("400x400")

# Add image button
img_button = Button(root, text="Select Image", command=open_image)
img_button.pack(pady=10)

# Add secret message label and entry
secret_label = Label(root, text="Enter Secret Message:")
secret_label.pack(pady=5)
secret_entry = Entry(root, width=40)
secret_entry.pack()

# Add save button
save_button = Button(root, text="Save Encrypted Image", command=save_image)
save_button.pack(pady=10)

# Run the GUI
root.mainloop()

