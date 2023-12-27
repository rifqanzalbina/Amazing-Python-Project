import cv2
import numpy as np
import tkinter as tk
from tkinter.filedialog import *

window = tk.Tk()
window.title("Border Extraction")
window.geometry("800x600")
label = tk.Label(window, text="Choose An Image").grid(row=0, column=0)

photo = askopenfilename()
img = cv2.imread(photo)
n, l, m = img.shape
size = (n, l)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

thresold_value = 20
ret, thresh = cv2.threshold(gray, thresold_value, 255, 0)

kernel = np.ones((5, 5), np.uint8)
dilated = cv2.dilate(thresh, kernel, iterations=100)
eroded = cv2.erode(thresh, kernel, iterations=10)

bordered = dilated - eroded
bordered = cv2.resize(bordered, size)
cv2.imshow("Border / Outline ", bordered)
cv2.imwrite("Output.png", bordered)
cv2.waitKey(0)
cv2.destroyAllWindows()

window.mainloop()