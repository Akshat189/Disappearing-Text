from tkinter import Tk, Text, Label, END, Canvas
from PIL import ImageTk, Image
import tkinter

import re
from PIL import Image, ImageTk
#
# Constants
RED = (150, 39, 150)
DARK_PINK = (191, 75, 191)
MEDIUM_PINK = (209, 105, 209)
LIGHT_PINK = (217, 143, 217)
LIGHTEST_PINK = (235, 197, 220)

COLOURS = [LIGHTEST_PINK, LIGHT_PINK, MEDIUM_PINK, DARK_PINK, RED]

# Globals
timer = 0
has_written = False


# Methods
def transform_rgb_to_hex(rgb):
    r, g, b = rgb
    return f'#{r:02x}{g:02x}{b:02x}'


def countdown():
    global has_written

    if has_written:
        global timer

        timer += 1

        # timer_label.config(text=timer)
        canvas.itemconfig(timer_label, text=timer)
        text_window.config(highlightcolor=transform_rgb_to_hex(COLOURS[timer - 1]),
                           highlightbackground=transform_rgb_to_hex(COLOURS[timer-1]),
                           bg=transform_rgb_to_hex(COLOURS[timer-1]))

        if timer >= 5:
            delete_text()
            has_written = False

        tk.after(1000, countdown)


def reset_timer():
    global timer
    timer = 0


def check_flag(event=None):
    global has_written

    if has_written:
        reset_timer()
    else:
        has_written = True
        text_window.config(highlightbackground="white", highlightcolor="white")
        countdown()


def delete_text():
    words = text_window.get("1.0", "end-1c")
    wordcount = len(re.findall("\w+", words))

    # timer_label.config(text=f"Your timer has ended. You've written {wordcount} words.")
    canvas.itemconfig(timer_label, text=f"Your timer has ended. You've written {wordcount} words.")
    text_window.delete("1.0", END)

    reset_timer()




# GUI
tk = Tk()

tk.title("The Most Dangerous Writing Snake")
tk.geometry("1092x736")

bg = ImageTk.PhotoImage(file="new_keyboard.jpg")
# #
canvas = Canvas(tk, width=1092, height=736)
# canvas.create_image(0,0,image=bg, anchor="nw")
canvas.pack(expand=True, fill = "both")



# Display image
canvas.create_image(0, 0, image=bg, anchor="nw")
canvas.create_text(550, 100, text="Don't stop.", font=("Courier", 40, "bold"), fill="white")


text_window = Text(tk, height=20, width=100, highlightthickness=1)

# text_label = Label(tk, text="Don't stop.")
# timer_label = Label(tk)

text_window.bind("<Key>", check_flag)
# text_label.config(font=("Courier", 14))
canvas.create_window(550, 300, window=text_window)

browse_text = tkinter.StringVar()
timer_label = canvas.create_text(550, 500, text="0", fill="white")
#
# text_label.pack(pady=50)
# text_window.pack()
# timer_label.pack()






# Main Loop
tk.mainloop()
























