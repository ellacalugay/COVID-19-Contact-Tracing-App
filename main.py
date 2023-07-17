# Ella Lureen C. Calugay | BSCPE 1-5 | Final Project

# Pseudocode
import tkinter as tk
from PIL import ImageTk, Image
# Import the UserInformation class from contact_tracing.py
from contact_tracing import UserInformation

# Define the main function
def main():
    # Create an instance of the UserInformation class
    user_info = UserInformation()

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

    # Access the collected user information through the instance's attributes
    print("User Information:")
    print(f"Name: {user_info.name}")
    print(f"Course and Year: {user_info.course_year}")

# Call the main function when the "Add Entry" button is clicked
def add_entry():
    main()

def search_entry():
    # Search entry functionality
    pass

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