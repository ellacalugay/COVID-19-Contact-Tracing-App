# Ella Lureen C. Calugay | BSCPE 1-5 | Final Project

# Pseudocode
# Import tkinter
import tkinter as tk
from PIL import ImageTk, Image

class FrontPage():
    def main_window():
        # Create the main window
        window = tk.Tk()
        window.title("COVID Tracing App")

        # Set the window size and position
        window.geometry("850x650")

        # Load the background image
        image_path = "F:\\2nd sem\\OOP\\FINAL PROJ\\bg img.png"
        original_image = Image.open(image_path)
        resized_image = original_image.resize((850, 650))  
        background_image = ImageTk.PhotoImage(resized_image)

        # Create a canvas to display the background image
        canvas = tk.Canvas(window, width=500, height=300)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=background_image, anchor="nw")

        # Create add entry button.
        add_button = tk.Button(window, text="Add Entry", command=add_entry, height=3, bg="yellow", fg="black", font=("Arial", 10, "bold"))
        add_button.place(x=450, y=270, width=200)

        # Create search entry button.
        search_button = tk.Button(window, text="Search Entry", command=search_entry, height=3, bg="pink", fg="black", font=("Arial", 10, "bold"))
        search_button.place(x=450, y=340, width=200)

        # Create All about covid 19 button.
        search_button = tk.Button(window, text="All About COVID 19", command=search_entry, height=2, bg="red", fg="black", font=("Arial", 10, "bold"))
        search_button.place(x=350, y=535, width=200)

        # Create App policies button.
        search_button = tk.Button(window, text="App Policies", command=search_entry, height=2, bg="light blue", fg="black", font=("Arial", 10, "bold"))
        search_button.place(x=570, y=535, width=200) 

        # Run the main window loop.
        window.mainloop()

    # Create add entry
    def add_entry():
        # Add entry functionality
        pass

    # Create search entry
    def search_entry():
        # Search entry functionality
        pass

    # Call the main_window function to run the application.
    main_window()

if __name__ == "__main__":
    app = FrontPage()
    app.run()