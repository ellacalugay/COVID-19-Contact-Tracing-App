# Ella Lureen C. Calugay | BSCPE 1-5 | Final Project

# Pseudocode
# Import necessary modules
import tkinter as tk
from PIL import ImageTk, Image

# Create class for notify frame
class NotifyFrame(tk.Toplevel):
    def __init__(self, master=None):
        tk.Toplevel.__init__(self, master)
        self.title("Notification")

        # Set the background image
        self.add_image_path = "F:\\2nd sem\\OOP\\FINAL PROJ\\notified.png"
        self.add_original_image = Image.open(self.add_image_path)
        self.add_resized_image = self.add_original_image.resize((850, 650))
        self.background_image = ImageTk.PhotoImage(self.add_resized_image)

        canvas = tk.Canvas(self, width=850, height=650)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=self.background_image, anchor="nw")

        # Create an exit button
        ok_button = tk.Button(self, text="OK", command=self.close_window, bg='#CD5555', font=('new times roman', 12))
        ok_button.place(x=408, y=435)

        # Create a turn back button
        back_button = tk.Button(self, text='Back', command=self.go_to_main_window, bg='light pink', font=('new times roman', 12))
        back_button.place(x=20, y=20)

     # Define the exit window. This home window will exit the program
    def close_window(self):
        self.master.destroy()

    # Go back to the main window.
    def go_to_main_window(self):
        self.destroy()
        self.master.deiconify()  # This will show the main window again.
    
    # Go back to the main window.
    def open_main_window(self):
        app = self.FrontPage()
        app.main_window()

# End of code.