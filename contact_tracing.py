# Ella Lureen C. Calugay | BSCPE 1-5 | Final Project

# Pseudocode
# Import necessary modules
import tkinter as tk
from PIL import ImageTk, Image
from add_entry import AddEntry
from search_entry import SearchEntry
from all_about_covid19 import AllAboutCovid
from app_policies import AppPolicies

class FrontPage():
    def __init__(self):
        # Create the main window
        self.window = tk.Tk()
        self.window.title("COVID Tracing App")

        # Set the window size and position
        self.window.geometry("850x650")

        # Load the background image
        image_path = "F:\\2nd sem\\OOP\\FINAL PROJ\\bg img.png"
        original_image = Image.open(image_path)
        resized_image = original_image.resize((850, 650))  
        background_image = ImageTk.PhotoImage(resized_image)

        # Create a canvas to display the background image
        canvas = tk.Canvas(self.window, width=500, height=300)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=background_image, anchor="nw")

        # Create add entry button.
        add_button = tk.Button(self.window, text="Add Entry", command=self.add_entry, height=3, bg="yellow", fg="black", font=("Arial", 10, "bold"))
        add_button.place(x=450, y=290, width=200)

        # Create search entry button.
        search_button = tk.Button(self.window, text="Search Entry", command=self.search_entry, height=3, bg="pink", fg="black", font=("Arial", 10, "bold"))
        search_button.place(x=450, y=360, width=200)

        # Create All about covid 19 button.
        covid19_button = tk.Button(self.window, text="All About COVID 19", command=self.covid_entry, height=2, bg="red", fg="black", font=("Arial", 10, "bold"))
        covid19_button.place(x=350, y=580, width=200)

        # Create App policies button.
        app_policies_button = tk.Button(self.window, text="App Policies", command=self.app_policies_entry, height=2, bg="light blue", fg="black", font=("Arial", 10, "bold"))
        app_policies_button.place(x=570, y=580, width=200) 

        # Run the main window loop.
        self.window.mainloop()

    # Create add entry
    def add_entry(self):
        # Add entry functionality
        info_frame = AddEntry()
        info_frame.place(x=0, y=0, relwidth=1, relheight=1)

    # Create search entry
    def search_entry(self):
        # Search entry functionality
        search_frame = SearchEntry()
        search_frame.place(x=0, y=0, relwidth=1, relheight=1)

    # Create covid19 entry
    def covid_entry(self):
        # All About COVID 19 functionality
        covid_frame = AllAboutCovid(self.window)
        covid_frame.place(x=0, y=0, relwidth=1, relheight=1)
    
    # Create App Policies entry
    def app_policies_entry(self):
         # App Policies functionality
        app_policies_frame = AppPolicies(self.window)
        app_policies_frame.place(x=0, y=0, relwidth=1, relheight=1)

    def close_window(self):
        self.window.destroy()
    
    def run(self):
        self.window.mainloop()

# Create the main window
if __name__ == "__main__":
    app = FrontPage()
    app.run()

# End of code.