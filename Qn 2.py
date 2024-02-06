import cv2
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk

def decimal_to_binary(decimal_number):
    # Convert to integer before converting to binary
    binary_number = bin(int(decimal_number))[2:]  # Remove the '0b' prefix
    return binary_number.zfill(10)

def convert_and_display():
    decimal_number = float(decimal_entry.get())
    binary_number = decimal_to_binary(decimal_number)
    binary_result_label.config(text=f"Binary Number: {binary_number}")

    # Display the binary number using OpenCV
    image = np.zeros((100, 300, 3), dtype=np.uint8)
    cv2.putText(image, binary_number, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    photo = ImageTk.PhotoImage(image=Image.fromarray(image))
    cv2.imshow("Binary Number", cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
    cv2.waitKey(0)

# Create the main window
root = tk.Tk()
root.title("Decimal to Binary Converter")

# GUI components
decimal_label = tk.Label(root, text="Enter Decimal Number:")
decimal_entry = tk.Entry(root)
convert_button = tk.Button(root, text="Convert", command=convert_and_display)
binary_result_label = tk.Label(root, text="Binary Number: ")

# Layout
decimal_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
decimal_entry.grid(row=0, column=1, padx=10, pady=5)
convert_button.grid(row=1, column=0, columnspan=2, pady=5)
binary_result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

# Run the main loop
root.mainloop()
