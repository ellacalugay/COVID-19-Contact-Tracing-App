# Ella Lureen C. Calugay | BSCPE 1-5 | Final Project

# Pseudocode
# Import necessary modules
import tkinter as tk
from PIL import ImageTk, Image

# Create a class named Search Entry
class SearchEntry(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        # Set the image background
        self.add_image_path = "F:\\2nd sem\\OOP\\FINAL PROJ\\searchentry.png"
        self.add_original_image = Image.open(self.add_image_path)
        self.add_resized_image = self.add_original_image.resize((850, 650))
        self.background_image = ImageTk.PhotoImage(self.add_resized_image)

        canvas = tk.Canvas(self, width=850, height=650)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=self.background_image, anchor="nw")

        # Create enter data button
        self.search_label = tk.Label(self, text="Enter Registered Name:",bg="#FFE1FF", height=2, font=("Tahoma", 10, "bold"))
        self.search_label.place(x=41, y=82)
        self.search_entry = tk.Text(self, width=39, height=2, font=("Lucida Bright", 12, "bold"))
        self.search_entry.place(x=200, y=82)

        # Create search button
        search_button = tk.Button(self, text="SEARCH",bg="#FFE1FF", height=2, font=("Tahoma", 10, "bold"),  command=self.perform_search)
        search_button.place(x=600, y=82) 
                                
# Create canvass for the results
# Create canvass for the another results
# Create exit button
# Create back button
# Exit the window. This will exit the program.

 # Define the perform search
    def perform_search(self):
            
            self.result1_canvas.delete("all")
            self.result2_canvas.delete("all")