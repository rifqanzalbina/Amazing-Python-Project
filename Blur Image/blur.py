from tkinter.filedialog import *
from tkinter.messagebox import askyesno
import tkinter as tk
import cv2

window = tk.Tk()
window.title("Image Blur")
window.geometry('350x200')
label = tk.Label(window, text="Choose an option").grid(row=0, column=1)


def blur1():
    photo = askopenfilename()
    img = cv2.imread(photo)
    avgblur = cv2.blur(img, (5, 5))

    cv2.imshow("Image", img)
    cv2.imshow("Average blur", avgblur)

    save_option = askyesno("Save", "Do you want to save the blurred image?")
    if save_option:
        save_filename = asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        cv2.imwrite(save_filename, avgblur)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def fx(x):
    return


def blur2():
    photo = askopenfilename()
    img = cv2.imread(photo)

    cv2.namedWindow("Gaussian Blur", cv2.WINDOW_NORMAL)

    cv2.createTrackbar("kernelSize", 'Gaussian Blur', 1, 7, fx)

    g = cv2.getTrackbarPos("kernelSize", 'Gaussian Blur')

    if g == 3 or g == 5 or g == 7:
        gaussblur = cv2.GaussianBlur(img, (g, g), 0)
    else:
        gaussblur = cv2.GaussianBlur(img, (3, 3), 0)

    cv2.imshow("Image", img)
    cv2.imshow("Gaussian Blur", gaussblur)

    save_option = askyesno("Save", "Do you want to save the blurred image?")
    if save_option:
        save_filename = asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        cv2.imwrite(save_filename, gaussblur)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def blur3():
    photo = askopenfilename()
    img = cv2.imread(photo)
    medianblur = cv2.medianBlur(img, 5)

    cv2.imshow("Image", img)
    cv2.imshow("Median blur", medianblur)

    save_option = askyesno("Save", "Do you want to save the blurred image?")
    if save_option:
        save_filename = asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        cv2.imwrite(save_filename, medianblur)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


rad1 = tk.Radiobutton(window, text='average blur', value=1, command=blur1)
rad2 = tk.Radiobutton(window, text='gaussian blur', value=2, command=blur2)
rad3 = tk.Radiobutton(window, text='median blur', value=3, command=blur3)

rad1.grid(row=1, column=0)
rad2.grid(row=1, column=1)
rad3.grid(row=1, column=2)

window.mainloop()
