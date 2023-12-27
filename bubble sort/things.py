# functions.py

from tkinter import Canvas, messagebox
import random
import time

def draw_data(canvas, data, colors):
    canvas.delete("all")
    canvas_height = 500
    canvas_width = 800
    x_width = canvas_width / (len(data) + 1)
    offset = 20
    spacing = 10

    # Normalizing Height Bars
    normalize_data = [i / max(data) for i in data]

    for i, rec_height in enumerate(normalize_data):
        x_initial = i * x_width + offset + spacing
        y_initial = canvas_height - rec_height * 460

        x_final = (i+1) * x_width + offset
        y_final = canvas_height

        canvas.create_rectangle(x_initial, y_initial,
                                x_final, y_final, fill=colors[i])
        canvas.create_text(x_initial + 2, y_initial,
                           anchor="sw", text=str(data[i]))

    # Updating Canvas
    canvas.update_idletasks()


def bubble_sort(canvas, data, speed):
    for i in range(len(data)-1):
        for j in range(len(data) - i - 1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
            draw_data(canvas, data, ["yellow" if x == j or x == j +
                                     1 else "red" for x in range(len(data))])
            time.sleep(speed)

    draw_data(canvas, data, ["green" for x in range(len(data))])


def generate_array(data, canvas, min_val, size_val, max_val):
    # Reading user inputs
    if min_val > max_val:
        messagebox.showwarning(
            message="Max. value should not be less than Min. value")
        min_val, max_val = max_val, min_val
        return False

    data.clear()

    for i in range(size_val):
        data.append(random.randrange(min_val, max_val + 1))

    draw_data(canvas, data, ["red" for x in range(len(data))])
    return True


def reset_array(data, canvas, unsorted_data):
    """
    Function that resets the current sorted array
    """
    data.clear()
    data.extend(unsorted_data)
    draw_data(canvas, data, ["red" for x in range(len(data))])
