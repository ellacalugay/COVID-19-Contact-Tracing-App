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
        self.personal_info_label = tk.Label(self, text="PERSONAL INFORMATION", height=2, font=("Helvetica", 10, "bold"))
        self.personal_info_label.place(x=15, y=10)
        self.personal_info_label.config(bg="#B0C4DE")
        # Get user's name
        self.name = tk.Label(self, text="NAME: ", height=1, font=("Arial", 10, "bold"))
        self.name.place(x=17, y=50)
        self.name.config(bg="#FFF68F")
        
        # Name Input
        self.name_entry = tk.Entry(self, width=40)
        self.name_entry.place(x=70, y= 51)
        # Set initial text
        self.name_entry.insert(0, "FIRST NAME/MIDDLE NAME/SURNAME")  
        self.name_entry.bind("<FocusIn>", self.clear_name_text)
        self.name_entry.config(fg="gray", bg="#FFF8DC")

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

    # Display text will be gone if the user click the entry

    def clear_name_text(self, event):
        self.name_entry.delete(0, tk.END)
        self.name_entry.config(fg="black")