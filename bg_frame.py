# Ella Lureen C. Calugay | BSCPE 1-5 | Final Project

# Pseudocode
# Import necessary modules
import tkinter as tk
from PIL import ImageTk, Image

# Create class for background frame
class BackgroundFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.load_background()

    def load_background(self):
        # Set the background image
        image_path = "F:\\2nd sem\\OOP\\FINAL PROJ\\entry bg.png"
        original_image = Image.open(image_path)
        resized_image = original_image.resize((850, 650))
        self.background_image = ImageTk.PhotoImage(resized_image)

        # Create a canvas to display the background image
        canvas = tk.Canvas(self.master, width=850, height=650)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=self.background_image, anchor="nw")

# Set the background image
# Create an exit button
# Create a turn back button
# Exit the window. This will exit the program.