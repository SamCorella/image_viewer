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
        initialdir="/",
        )

    file = Image.open(filename)

    if file.width > 1000:
        file = file.resize((1000, file.height * 1000 // file.width))
    elif file.height > 1000:
        file = file.resize((file.width * 1000 // file.height, 1000))

    img = ImageTk.PhotoImage(file)
    images.append(img)
    cursor = len(images) - 1
    display_image(img)

def display_image(img):
    global lbl_image

    if len(images) > 1:
        lbl_image.grid_forget()

    lbl_image = tk.Label(image=img)
    lbl_image.grid(row=1, column=0)
    lbl_index = tk.Label(text=f"{cursor + 1} / {len(images)}")
    lbl_index.grid(row=0, column=0)

def forward():
    global cursor
    if cursor < len(images) - 1:
        cursor += 1
        display_image(images[cursor])

def back():
    global cursor
    if cursor > 0:
        cursor -= 1
        display_image(images[cursor])

lbl_index = tk.Label()
lbl_image = tk.Label(text="Display an image here!", width=15, height=15)
frm_buttons = tk.Frame(master=window)

btn_back = tk.Button(
    master=frm_buttons,
    text="<<",
    command=back,
    )

btn_addImage = tk.Button(
    master=frm_buttons,
    text="Add Image",
    command=open_image,
    )

btn_forward = tk.Button(
    master=frm_buttons,
    text=">>",
    command=forward,
    )

lbl_index.grid(row=0, column=0)
lbl_image.grid(row=1, column=0)
frm_buttons.grid(row=2, column=0)
btn_back.grid(row=0, column=0)
btn_addImage.grid(row=0, column=1)
btn_forward.grid(row=0, column=2)

window.mainloop()