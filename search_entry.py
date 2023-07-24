# Ella Lureen C. Calugay | BSCPE 1-5 | Final Project

# Pseudocode
# Import necessary modules
import tkinter as tk
from PIL import ImageTk, Image
import csv

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
        # Create entry button
        self.search_entry = tk.Text(self, width=39, height=2, font=("Lucida Bright", 12, "bold"))
        self.search_entry.place(x=200, y=82)

        # Create search button
        search_button = tk.Button(self, text="SEARCH",bg="#FFE1FF", height=2, font=("Tahoma", 10, "bold"),  command=self.perform_search)
        search_button.place(x=750, y=82) 

        # Create the canvas to display the search results
        self.result1_canvas = tk.Canvas(self, width=395, height=400, bg="light pink")
        self.result1_canvas.place(x=15, y=150)

        self.result2_canvas = tk.Canvas(self, width=395, height=400, bg="light pink")
        self.result2_canvas.place(x=435, y=150)

        # Create exit button
        ok_button = tk.Button(self.master, text="OK", command=self.close_window,bg='#CD5555', font=('new times roman', 12))
        ok_button.place(x=405, y=580)

# Exit the window. This will exit the program.
     # Define the exit window. This home window will exit the program
    def close_window(self):
        self.master.destroy()

 # Define the perform search
    # Inside the perform_search method of SearchEntry class
    def perform_search(self):
        # Clear the canvas before displaying new search results
        self.result1_canvas.delete("all")
        self.result2_canvas.delete("all")

        # Get the entered name for search
        search_name = self.search_entry.get("1.0", "end-1c").strip()

        # Initialize 'found' variable with False
        found = False

        # Search the name in the CSV file
        with open('entry.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == search_name:
                    found = True
                    # Create value for result
                    result1 = f"PERSONAL INFORMATION\nName: {row[0]}\nAge: {row[1]}\nSex: {row[2]}\nResidential Address: {row[3]}\nContact Number: {row[4]}\nEmail Address: {row[5]}\n\n"
                    result1 += f"\n\nEMERGENCY INFORMATION\nContact Person Name: {row[6]}\nRelationship: {row[7]}\nContact Number: {row[8]}\nEmail Address: {row[9]}\n\n"
                    
                    result2 = f"HEALTH DECLARATION\nHave you received covid 19 vaccine shot: {row[10]}\nHave you been tested for COVID-19? {row[11]}\n\n"
                    print("\n")
                    # Get the selected symptoms
                    selected_symptoms = []
                    if row[12] == "Yes":
                        if row[13] == "Fever":
                            selected_symptoms.append("Fever")
                        if row[14] == "Cough":
                            selected_symptoms.append("Cough")
                        if row[15] == "Sore throat":
                            selected_symptoms.append("Sore throat")
                    result2 += f"\n\nRISK ASSESSMENT\nHave you experienced any of the following symptoms? {row[12]}\nHave you recently encountered a COVID-19 carrier? {row[13]}\n\n"
                    print("\n")
                    result2 += f"\n\nTRAVEL HISTORY\nHave you traveled to any high-risk areas recently? {row[14]}\nHave you traveled internationally in the past 14 days? {row[15]}\nHave you recently been to a large gathering or an event? {row[16]}"
                    
                    # Output the search results to the respective canvas
                    self.result1_canvas.create_text(10, 10, anchor="nw", text=result1, font=("Franklin Gothic Demi", 10), fill="black")
                    self.result2_canvas.create_text(10, 10, anchor="nw", text=result2, font=("Franklin Gothic Demi", 10), fill="black")
                    # Exit the loop once the name is found
                    break

        if not found:
            self.result1_canvas.create_text(10, 10, anchor="nw", text="Sorry. Name not found. No information available.", font=("Adobe Caslon Pro", 11, "bold"), fill="red")
            self.result2_canvas.create_text(10, 10, anchor="nw", text="")