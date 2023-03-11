import tkinter as tk
from tkinter import filedialog as fd
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Image Viewer")
window.resizable(width=False, height=False)

images = []
cursor = 0

def open_image():
    global cursor
    filename = fd.askopenfilename(
        title="Select an image",
        initialdir="/Users/samc/Pictures",
        )

    img = ImageTk.PhotoImage(Image.open(filename))
    images.append(img)
    cursor = len(images) - 1
    display_image(img)

def display_image(img):
    lbl_image = tk.Label(image=img)
    lbl_image.grid(row=0, column=0)

def next_image():
    global cursor
    if cursor < len(images) - 1:
        cursor += 1
        lbl_image.grid_forget()
        display_image(images[cursor])

def previous_image():
    global cursor
    if cursor > 0:
        cursor -= 1
        lbl_image.grid_forget()
        display_image(images[cursor])

lbl_image = tk.Label()
frm_buttons = tk.Frame(master=window)

btn_back = tk.Button(
    master=frm_buttons,
    text="<<",
    command=previous_image,
    )

btn_addImage = tk.Button(
    master=frm_buttons,
    text="Add Image",
    command=open_image,
    )

btn_forward = tk.Button(
    master=frm_buttons,
    text=">>",
    command=next_image,
    )

frm_buttons.grid(row=1, column=0)
btn_back.grid(row=0, column=0)
btn_addImage.grid(row=0, column=1)
btn_forward.grid(row=0, column=2)

window.mainloop()