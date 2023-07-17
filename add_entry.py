# Ella Lureen C. Calugay | BSCPE 1-5 | Final Project

# Pseudocode
# Import necessary modules
import tkinter as tk
from PIL import ImageTk, Image
from bg_frame import BackgroundFrame

# Create a class for add entry
class AddEntry(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        
        # Load and display the background image in the AddEntry frame
        self.add_image_path = "F:\\2nd sem\\OOP\\FINAL PROJ\\entry bg.png"
        self.add_original_image = Image.open(self.add_image_path)
        self.add_resized_image = self.add_original_image.resize((850, 650))
        self.background_image = ImageTk.PhotoImage(self.add_resized_image)

        canvas = tk.Canvas(self, width=850, height=650)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=self.background_image, anchor="nw")

    # Create Personal Information Label
        # Get user's name
        # Get user's age
        # Get user's gender
        # Get user's residential address

    # Create Contact Information label
        # Get user's contact number
        # Get user's email address

    # Create Emergency Information label
        # Get user's name of guardian
        # Get user's realationship to the guardian
        # Get user's guardian contact number
        # Get user's guardian email address

    # Create Risk Assessment label
        # Ask if the user experienced any of the following symptoms: fever, cough, shortness of breath, sore throat, loss of taste or smell, or body aches
        # Ask if the user have been in close contact with someone who has tested positive for COVID-19.

    # Create Travel History label
        # Ask if the user have traveled to any high-risk areas recently.
        # Ask if the user have traveled internationally in the past 14 days.
        # Ask if the user have recently attended large gatherings or events.

    # Create Health Declaration label
        # Ask if the user's received covid vaccine shot.
        # Ask if the user had any symptoms in the past 14 days?
        # Ask if the user have been tested for COVID-19? 