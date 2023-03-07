from tkinter import *
from tkinter import filedialog, messagebox
import cv2

def open_file():
    global file_path
    file_path = filedialog.askopenfilename(title="Select File", filetypes=[("Video Files", "*.mp4 *.avi")])

def save_video():
    global secret_entry, file_path
    if secret_entry.get() == '':
        messagebox.showwarning("Warning", "Secret message cannot be empty.")
        return
    if file_path is None:
        messagebox.showwarning("Warning", "Please select a video.")
        return
    cap = cv2.VideoCapture(file_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    save_path = filedialog.asksaveasfilename(defaultextension=".mp4")
    out = cv2.VideoWriter(save_path, fourcc, fps, frame_size)

    message = secret_entry.get()
    message_bits = ''.join(format(ord(c), '08b') for c in message) + '11111111'

    idx = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        for i in range(frame_size[0]):
            for j in range(frame_size[1]):
                r, g, b = frame[j, i]
                if idx < len(message_bits):
                    frame[j, i] = (r & 0xfe | int(message_bits[idx]), g, b)
                    idx += 1
        out.write(frame)

    cap.release()
    out.release()
    messagebox.showinfo("Done", "Video saved with encrypted message.")

# Create GUI window
root = Tk()
root.title("Steganography Program")
root.geometry("400x400")

# Add file button
file_button = Button(root, text="Select Video", command=open_file)
file_button.pack(pady=10)

# Add secret message label and entry
secret_label = Label(root, text="Enter Secret Message:")
secret_label.pack(pady=5)
secret_entry = Entry(root, width=40)
secret_entry.pack()

# Add save button
save_button = Button(root, text="Save Encrypted Video", command=save_video)
save_button.pack(pady=10)

# Run the GUI
root.mainloop()

