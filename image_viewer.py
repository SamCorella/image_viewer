import tkinter as tk

window = tk.Tk()
window.title("Image Viewer")
window.resizable(width=False, height=False)

lbl_image = tk.Label()
frm_buttons = tk.Frame(master=window)

btn_enter = tk.Button(
    master=frm_buttons,
    text="Select Image",
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