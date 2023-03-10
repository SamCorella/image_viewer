import tkinter as tk
from tkinter import filedialog as fd
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Image Viewer")
window.resizable(width=False, height=False)

def select_image():
    filename = fd.askopenfilename(
        mode="r",
        initialdir="/",
        )
    
    load = Image.open(filename)
    img = ImageTk.PhotoImage(load)
    lbl_image = tk.Label(image=img)
    lbl_image.grid(row=0, column=0)

frm_buttons = tk.Frame(master=window)

btn_enter = tk.Button(
    master=frm_buttons,
    text="Select Image",
    command=select_image,
    )

btn_back = tk.Button(
    master=frm_buttons,
    text="<<",
    )

btn_forward = tk.Button(
    master=frm_buttons,
    text=">>",
    )

frm_buttons.grid(row=1, column=0)
btn_back.grid(row=0, column=0)
btn_enter.grid(row=0, column=1)
btn_forward.grid(row=0, column=2)

window.mainloop()