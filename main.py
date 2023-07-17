# Ella Lureen C. Calugay | BSCPE 1-5 | Final Project

# Pseudocode
# Importing necessary modules
import tkinter as tk
from PIL import Image, ImageTk

# Import the UserInformation class from user_information.py
from contact_tracing import UserInformation

# Define # Function to show the personal information window
def show_personal_info_window():
    personal_info_window = tk.Toplevel(window)
    personal_info_window.title("Personal Information")

    user_info = UserInformation()

    # Label to display instructions
    label = tk.Label(personal_info_window, text="Please provide your personal information:")
    label.pack()

    # Entry fields for personal information
    entry_name = tk.Entry(personal_info_window)
    entry_name.pack()
    label_name = tk.Label(personal_info_window, text="Name:")
    label_name.pack()

    entry_age = tk.Entry(personal_info_window)
    entry_age.pack()
    label_age = tk.Label(personal_info_window, text="Age:")
    label_age.pack()

    # Function to get the user's information and update the UserInformation instance
    def get_personal_info():
        user_info.personal_information["name"] = entry_name.get()
        user_info.personal_information["age"] = int(entry_age.get())

    # Close the personal_info_window after gathering the information
    personal_info_window.destroy()
    # Call the methods to ask for the user's information
    user_info.ask_personal_information()
    user_info.ask_covid_vaccination_type()
    user_info.ask_health_declaration()
    user_info.ask_risk_assessment()
    user_info.ask_travel_history()
    user_info.ask_contact_log()
    user_info.ask_covid19_testing()
    user_info.ask_emergency_information()
    user_info.ask_receive_notifications()

# Create the main window
window = tk.Tk()
window.title("COVID Tracing App")

# Set the window size and position
window.geometry("800x600")

# Load the background image
image_path = "F:\\2nd sem\\OOP\\FINAL PROJ\\bg img.png"
original_image = Image.open(image_path)
resized_image = original_image.resize((800, 600))  # Adjust the desired size here
background_image = ImageTk.PhotoImage(resized_image)

# Create a canvas to display the background image
canvas = tk.Canvas(window, width=500, height=300)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=background_image, anchor="nw")

# Add Entry Button
add_button = tk.Button(window, text="Add Entry", command=add_entry, height=3, bg="yellow", fg="black", font=("Arial", 10, "bold"))
add_button.place(x=450, y=270, width=200)

# Search Entry Button
search_button = tk.Button(window, text="Search Entry", command=search_entry, height=3, bg="pink", fg="black", font=("Arial", 10, "bold"))
search_button.place(x=450, y=340, width=200)

# COVID 19 Button
search_button = tk.Button(window, text="All About COVID 19", command=search_entry, height=2, bg="red", fg="black", font=("Arial", 10, "bold"))
search_button.place(x=350, y=535, width=200)

# App Policies Button
search_button = tk.Button(window, text="App Policies", command=search_entry, height=2, bg="light blue", fg="black", font=("Arial", 10, "bold"))
search_button.place(x=570, y=535, width=200) 

# Run the main window loop
window.mainloop()



