# Ella Lureen C. Calugay | BSCPE 1-5 | Final Project

# Pseudocode
# Import necessary modules
import tkinter as tk
from PIL import ImageTk, Image
from bg_frame import BackgroundFrame
from tkinter import StringVar

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
        self.personal_info_label = tk.Label(self, text=" PERSONAL INFORMATION ", height=2, font=("Tahoma", 10, "bold"))
        self.personal_info_label.place(x=15, y=10)
        self.personal_info_label.config(bg="#FFE1FF")

        # Get user's name
        self.name = tk.Label(self, text="NAME: ", height=1, font=("Lucida Bright", 10, "bold"))
        self.name.place(x=17, y=56)
        self.name.config(bg="#EAEAEA")
        # Name Input
        self.name_entry = tk.Entry(self, width=40)
        self.name_entry.place(x=70, y= 56)
        # Set initial text
        self.name_entry.insert(0, " FIRST NAME/MIDDLE NAME/SURNAME")  
        self.name_entry.bind("<FocusIn>", self.clear_name_text)
        self.name_entry.config(fg="gray", bg="#FFFAFA", font=("Times", 11))

        # Get user's age
        self.age = tk.Label(self, text="AGE:    ", height=1, font=("Lucida Bright", 10, "bold"))
        self.age.place(x=17, y=80)
        self.age.config(bg="#EAEAEA")
        # Age Input
        self.age_entry = tk.Entry(self, width=40)
        self.age_entry.place(x=70, y= 80)
        # Set initial text
        self.age_entry.insert(0, " YOUR AGE")  
        self.age_entry.bind("<FocusIn>", self.clear_age_text)
        self.age_entry.config(fg="gray", bg="#FFFAFA", font=("Times", 11))

        # Get user's sex
        self.gender = tk.Label(self, text="SEX:     ", height=1, font=("Lucida Bright", 10, "bold"))
        self.gender.place(x=17, y=105)
        self.gender.config(bg="#EAEAEA")
        # Gender Input
        self.gender_entry = tk.Entry(self, width=40)
        self.gender_entry.place(x=70, y= 105)
        # Set initial text
        self.gender_entry.insert(0, " FEMALE/MALE")  
        self.gender_entry.bind("<FocusIn>", self.clear_sex_text)
        self.gender_entry.config(fg="gray", bg="#FFFAFA", font=("Times", 11))

        # Get user's residential address
        self.residential_address = tk.Label(self, text="RESID ADD: ", height=1, font=("Lucida Bright", 10, "bold"))
        self.residential_address.place(x=17, y=130)
        self.residential_address.config(bg="#EAEAEA")
        # Residential Address Input
        self.residential_address_entry = tk.Entry(self, width=36)
        self.residential_address_entry.place(x=100, y= 130)
        # Set initial text
        self.residential_address_entry.insert(0, " BARANGAY/CITY/PROVINCE")  
        self.residential_address_entry.bind("<FocusIn>", self.clear_resi_add_text)
        self.residential_address_entry.config(fg="gray", bg="#FFFAFA", font=("Times", 11))

    # Create Contact Information label
        self.contact_info_label = tk.Label(self, text=" CONTACT INFORMATION ", height=2, font=("Tahoma", 10, "bold"))
        self.contact_info_label.place(x=17, y=180)
        self.contact_info_label.config(bg="#FFE1FF")

        # Get user's contact number
        self.contact_num = tk.Label(self, text="CONTACT NUMBER: ", height=1, font=("Lucida Bright", 10, "bold"))
        self.contact_num.place(x=17, y=226)
        self.contact_num.config(bg="#EAEAEA")
        # Conatct Number Input
        self.contact_num_entry = tk.Entry(self, width=28)
        self.contact_num_entry.place(x=155, y= 226)
        # Set initial text
        self.contact_num_entry.insert(0, "09*********")  
        self.contact_num_entry.bind("<FocusIn>", self.clear_contact_num_text)
        self.contact_num_entry.config(fg="gray", bg="#FFFAFA", font=("Times", 11))
        
        # Get user's email address
        self.email_add = tk.Label(self, text="EMAIL ADDRESS:  ", height=1, font=("Lucida Bright", 10, "bold"))
        self.email_add.place(x=17, y=251)
        self.email_add.config(bg="#EAEAEA")
        # Email Address Input
        self.email_add_entry = tk.Entry(self, width=30)
        self.email_add_entry.place(x=140, y= 251)
        # Set initial text
        self.email_add_entry.insert(0, " juandelacruz@gmail.com")  
        self.email_add_entry.bind("<FocusIn>", self.clear_email_add_text)
        self.email_add_entry.config(fg="gray", bg="#FFFAFA", font=("Times", 11))

    # Create Emergency Information label
        self.emergency_info_label = tk.Label(self, text=" EMERGENCY INFORMATION ", height=2, font=("Tahoma", 10, "bold"))
        self.emergency_info_label.place(x=17, y=301)
        self.emergency_info_label.config(bg="#FFE1FF")

        # Get user's name of guardian
        self.guardian_name = tk.Label(self, text="NAME: ", height=1, font=("Lucida Bright", 10, "bold"))
        self.name.place(x=17, y=56)
        self.guardian_name.place(x=17, y=347)
        self.guardian_name.config(bg="#EAEAEA")
        # Guardian name Input
        self.guardian_name_entry = tk.Entry(self, width=40)
        self.guardian_name_entry.place(x=70, y=347)
        # Set initial text inside the Entry widget
        self.guardian_name_entry.insert(0, " FIRST NAME/MIDDLE NAME/SURNAME")
        self.guardian_name_entry.bind("<FocusIn>", self.clear_guardian_name_text)
        self.guardian_name_entry.config(fg="gray", bg="#FFFAFA", font=("Times", 11))

        # Get user's realationship to the guardian
        self.guardian_relationship = tk.Label(self, text="RELATIONSHIP:  ", height=1, font=("Lucida Bright", 10, "bold"))
        self.guardian_relationship.place(x=17, y=372)
        self.guardian_relationship.config(bg="#EAEAEA")
        # Guardian Relationship Input
        self.guardian_relationship_entry = tk.Entry(self, width=33)
        self.guardian_relationship_entry.place(x=122, y=372)
        # Set initial text inside the Entry widget
        self.guardian_relationship_entry.insert(0, " MOTHER/FATHER/SISTER,ETC.")
        self.guardian_relationship_entry.bind("<FocusIn>", self.clear_guardian_relationship_text)
        self.guardian_relationship_entry.config(fg="gray", bg="#FFFAFA", font=("Times", 11))

        # Get user's guardian contact number
        self.guardian_contact = tk.Label(self, text="CONTACT NUMBER:  ", height=1, font=("Lucida Bright", 10, "bold"))
        self.guardian_contact.place(x=17, y=397)
        self.guardian_contact.config(bg="#EAEAEA")
        # Guardian Contact Input
        self.guardian_contact_entry = tk.Entry(self, width=28)
        self.guardian_contact_entry.place(x=155, y=397)
        # Set initial text inside the Entry widget
        self.guardian_contact_entry.insert(0, " 09*********")
        self.guardian_contact_entry.bind("<FocusIn>", self.clear_guardian_contact_text)
        self.guardian_contact_entry.config(fg="gray", bg="#FFFAFA", font=("Times", 11))

        # Get user's guardian email address
        self.guardian_email_add = tk.Label(self, text="EMAIL ADDRESS:  ", height=1, font=("Lucida Bright", 10, "bold"))
        self.guardian_email_add.place(x=17, y=422)
        self.guardian_email_add.config(bg="#EAEAEA")
        # Guardian Email Address Input
        self.guardian_email_add_entry = tk.Entry(self, width=30)
        self.guardian_email_add_entry.place(x=140, y=422)
        # Set initial text inside the Entry widget
        self.guardian_email_add_entry.insert(0, " juandelacruz@gmail.com")
        self.guardian_email_add_entry.bind("<FocusIn>", self.clear_guardian_email_add_text)
        self.guardian_email_add_entry.config(fg="gray", bg="#FFFAFA", font=("Times", 11))

    # Create Risk Assessment label
        self.risk_assessment_label = tk.Label(self, text=" RISK ASSESSMENT ", height=2, font=("Tahoma", 10, "bold"))
        self.risk_assessment_label.place(x=400, y=10)
        self.risk_assessment_label.config(bg="#FFE1FF")
        # Ask if the user experienced any of the following symptoms: fever, cough, shortness of breath, sore throat, loss of taste or smell, or body aches
        self.symptoms = tk.Label(self, text=" Have you experienced any of the following symptoms:", font=("Tekton Pro", 10, "bold"))
        self.symptoms.place(x=400, y=55)
        self.symptoms.config(bg="#FFFAFA")

        # Create the symptoms choice variable
        self.fever_choice = StringVar()
        self.cough_choice = StringVar()
        self.shortness_of_breath_choice = StringVar()

        # Create fever checkbutton
        self.fever_checkbox = tk.Checkbutton(self, text="Fever", font=("Arial", 8), variable=self.fever_choice)
        self.fever_checkbox.place(x=400, y=80)
        self.fever_checkbox.config(bg="#FFFAFA")
        # Create cough checkbutton
        self.cough_checkbox = tk.Checkbutton(self, text="Cough", font=("Arial", 8), variable=self.cough_choice)
        self.cough_checkbox.place(x=400, y=110)
        self.cough_checkbox.config(bg="#FFFAFA")
        # Create shortness of breath checkbutton
        self.shortness_of_breath_checkbox = tk.Checkbutton(self, text="Shortness of breath", font=("Arial", 8), variable=self.shortness_of_breath_choice)
        self.shortness_of_breath_checkbox.place(x=400, y=140)
        self.shortness_of_breath_checkbox.config(bg="#FFFAFA")

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
    def clear_age_text(self, event):
        self.age_entry.delete(0, tk.END)
        self.age_entry.config(fg="black")
    def clear_sex_text(self, event):
        self.gender_entry.delete(0, tk.END)
        self.gender_entry.config(fg="black")
    def clear_resi_add_text(self, event):
        self.residential_address_entry.delete(0, tk.END)
        self.residential_address_entry.config(fg="black")
    def clear_contact_num_text(self, event):
        self.contact_num_entry.delete(0, tk.END)
        self.contact_num_entry.config(fg="black")
    def clear_email_add_text(self, event):
        self.email_add_entry.delete(0, tk.END)
        self.email_add_entry.config(fg="black")
    def clear_guardian_name_text(self, event):
        self.guardian_name_entry.delete(0, tk.END)
        self.guardian_name_entry.config(fg="black")
    def clear_guardian_relationship_text(self, event):
        self.guardian_relationship_entry.delete(0, tk.END)
        self.guardian_relationship_entry.config(fg="black")
    def clear_guardian_contact_text(self, event):
        self.guardian_contact_entry.delete(0, tk.END)
        self.guardian_contact_entry.config(fg="black")
    def clear_guardian_email_add_text(self, event):
        self.guardian_email_add_entry.delete(0, tk.END)
        self.guardian_email_add_entry.config(fg="black")