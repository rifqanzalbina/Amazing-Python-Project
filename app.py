# app.py

from tkinter import Tk, Frame, Label, Button, Scale, HORIZONTAL, Canvas # You Can Change This to 'fromt tkinter import *'
import things as fs

unsorted_data = data = []


def run_sort():
    """
    Function that runs the simulation on user click
    """
    global data
    fs.bubble_sort(canvas, data, speed_scale.get())


# Initializing the main program
main_prog = Tk()
main_prog.title("Bubble Sort Visualization")
main_prog.maxsize(800, 800)
main_prog.config(bg="grey")


# Creating user interface frame
UI_frame = Frame(main_prog, width=800, height=300, bg="grey")
UI_frame.grid(row=0, column=0)
Label(UI_frame, text="Let's learn Bubble Sort", bg="grey").grid(
    row=0, column=0, padx=5, pady=5, sticky="w")
Button(UI_frame, text="Start", command=run_sort,
       bg="green").grid(row=0, column=1, padx=5, pady=5)

speed_scale = Scale(UI_frame, from_=0.1, to=2.0, length=200, digits=2,
                    resolution=0.2, orient=HORIZONTAL, label="Select Speed", bg="ivory")
speed_scale.grid(row=0, column=2, padx=5, pady=5)

# Creating scale for array size
size_value = Scale(UI_frame, from_=0, to=30, resolution=1,
                   orient=HORIZONTAL, label="Select Size", bg="ivory")
size_value.grid(row=1, column=0, padx=5, pady=5, sticky="w")

# Creating scale for min. value of generated values
min_value = Scale(UI_frame, from_=0, to=100, resolution=10,
                  orient=HORIZONTAL, label="Select Min. value", bg="ivory")
min_value.grid(row=1, column=1, padx=5, pady=5, sticky="w")

# Creating scale for max. value of generated values
max_value = Scale(UI_frame, from_=0, to=500, resolution=10,
                  orient=HORIZONTAL, label="Select Max. value", bg="ivory")
max_value.grid(row=1, column=2, padx=5, pady=5, sticky="w")

# Generate random array button
Button(UI_frame, text="Generate", command=lambda: fs.generate_array(
    data, canvas, min_value.get(), size_value.get(), max_value.get()), bg="blue").grid(row=2, column=2, padx=5, pady=5)

# Reset the current array button
Button(UI_frame, text="Reset", command=lambda: fs.reset_array(
    data, canvas, unsorted_data), bg="blue").grid(row=2, column=1, padx=5, pady=5)

# Creating canvas for visualization
canvas = Canvas(main_prog, width=800, height=500, bg="white")
canvas.grid(row=1, column=0)

# Running the main program
main_prog.mainloop()
