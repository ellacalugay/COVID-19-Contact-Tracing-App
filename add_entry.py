# Ella Lureen C. Calugay | BSCPE 1-5 | Final Project

# Pseudocode
# Import necessary modules
import tkinter as tk
from PIL import ImageTk, Image
from notif_frame import NotifyFrame
from tkinter import StringVar
import csv

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
        self.contact_info_label.place(x=17, y=163)
        self.contact_info_label.config(bg="#FFE1FF")

        # Get user's contact number
        self.contact_num = tk.Label(self, text="CONTACT NUMBER: ", height=1, font=("Lucida Bright", 10, "bold"))
        self.contact_num.place(x=17, y=207)
        self.contact_num.config(bg="#EAEAEA")
        # Conatct Number Input
        self.contact_num_entry = tk.Entry(self, width=28)
        self.contact_num_entry.place(x=155, y= 207)
        # Set initial text
        self.contact_num_entry.insert(0, "09*********")  
        self.contact_num_entry.bind("<FocusIn>", self.clear_contact_num_text)
        self.contact_num_entry.config(fg="gray", bg="#FFFAFA", font=("Times", 11))
        
        # Get user's email address
        self.email_add = tk.Label(self, text="EMAIL ADDRESS:  ", height=1, font=("Lucida Bright", 10, "bold"))
        self.email_add.place(x=17, y=231)
        self.email_add.config(bg="#EAEAEA")
        # Email Address Input
        self.email_add_entry = tk.Entry(self, width=30)
        self.email_add_entry.place(x=140, y= 231)
        # Set initial text
        self.email_add_entry.insert(0, " juandelacruz@gmail.com")  
        self.email_add_entry.bind("<FocusIn>", self.clear_email_add_text)
        self.email_add_entry.config(fg="gray", bg="#FFFAFA", font=("Times", 11))

    # Create Emergency Information label
        self.emergency_info_label = tk.Label(self, text=" EMERGENCY INFORMATION ", height=2, font=("Tahoma", 10, "bold"))
        self.emergency_info_label.place(x=17, y=264)
        self.emergency_info_label.config(bg="#FFE1FF")

        # Get user's name of guardian
        self.guardian_name = tk.Label(self, text="NAME: ", height=1, font=("Lucida Bright", 10, "bold"))
        self.name.place(x=17, y=56)
        self.guardian_name.place(x=17, y=308)
        self.guardian_name.config(bg="#EAEAEA")
        # Guardian name Input
        self.guardian_name_entry = tk.Entry(self, width=40)
        self.guardian_name_entry.place(x=70, y=308)
        # Set initial text inside the Entry widget
        self.guardian_name_entry.insert(0, " FIRST NAME/MIDDLE NAME/SURNAME")
        self.guardian_name_entry.bind("<FocusIn>", self.clear_guardian_name_text)
        self.guardian_name_entry.config(fg="gray", bg="#FFFAFA", font=("Times", 11))

        # Get user's realationship to the guardian
        self.guardian_relationship = tk.Label(self, text="RELATIONSHIP:  ", height=1, font=("Lucida Bright", 10, "bold"))
        self.guardian_relationship.place(x=17, y=332)
        self.guardian_relationship.config(bg="#EAEAEA")
        # Guardian Relationship Input
        self.guardian_relationship_entry = tk.Entry(self, width=33)
        self.guardian_relationship_entry.place(x=122, y=332)
        # Set initial text inside the Entry widget
        self.guardian_relationship_entry.insert(0, " MOTHER/FATHER/SISTER,ETC.")
        self.guardian_relationship_entry.bind("<FocusIn>", self.clear_guardian_relationship_text)
        self.guardian_relationship_entry.config(fg="gray", bg="#FFFAFA", font=("Times", 11))

        # Get user's guardian contact number
        self.guardian_contact = tk.Label(self, text="CONTACT NUMBER:  ", height=1, font=("Lucida Bright", 10, "bold"))
        self.guardian_contact.place(x=17, y=356)
        self.guardian_contact.config(bg="#EAEAEA")
        # Guardian Contact Input
        self.guardian_contact_entry = tk.Entry(self, width=28)
        self.guardian_contact_entry.place(x=155, y=356)
        # Set initial text inside the Entry widget
        self.guardian_contact_entry.insert(0, " 09*********")
        self.guardian_contact_entry.bind("<FocusIn>", self.clear_guardian_contact_text)
        self.guardian_contact_entry.config(fg="gray", bg="#FFFAFA", font=("Times", 11))

        # Get user's guardian email address
        self.guardian_email_add = tk.Label(self, text="EMAIL ADDRESS:  ", height=1, font=("Lucida Bright", 10, "bold"))
        self.guardian_email_add.place(x=17, y=380)
        self.guardian_email_add.config(bg="#EAEAEA")
        # Guardian Email Address Input
        self.guardian_email_add_entry = tk.Entry(self, width=30)
        self.guardian_email_add_entry.place(x=140, y=380)
        # Set initial text inside the Entry widget
        self.guardian_email_add_entry.insert(0, " juandelacruz@gmail.com")
        self.guardian_email_add_entry.bind("<FocusIn>", self.clear_guardian_email_add_text)
        self.guardian_email_add_entry.config(fg="gray", bg="#FFFAFA", font=("Times", 11))

    # Create Health Declaration label
        self.health_declaration_label = tk.Label(self, text=" HEALTH DECLARATION ", height=2, font=("Tahoma", 10, "bold"))
        self.health_declaration_label.place(x=17, y=412)
        self.health_declaration_label.config(bg="#FFE1FF")

        # Ask if the user's received covid vaccine shot.
        self.vaccine_shot_label = tk.Label(self, text="Have you received covid 19 vaccine shot?", width=41,  font=("Tekton Pro", 10, "bold"))
        self.vaccine_shot_label.place(x=17, y=456)
        self.vaccine_shot_label.config(bg="#FFFAFA")
        # Create the vaccine shot choice variable
        self.vaccine_shot_choice = tk.StringVar()
        # Create choice 1
        self.vaccine_shot_choice1_radio = tk.Radiobutton(self, text="1st Dose", font=("Arial", 8), variable=self.vaccine_shot_choice, value="1")
        self.vaccine_shot_choice1_radio.place(x=30, y=482)
        self.vaccine_shot_choice1_radio.config(bg="#FFFAFA")
        # Create choice 2
        self.vaccine_shot_choice2_radio = tk.Radiobutton(self, text="2nd Dose - fully vaccinated", font=("Arial", 8), variable=self.vaccine_shot_choice, value="2")
        self.vaccine_shot_choice2_radio.place(x=130, y=482)
        self.vaccine_shot_choice2_radio.config(bg="#FFFAFA")
        # Create choice 3
        self.vaccine_shot_choice3_radio = tk.Radiobutton(self, text="1st Booster", font=("Arial", 8), variable=self.vaccine_shot_choice, value="3")
        self.vaccine_shot_choice3_radio.place(x=30, y=509)
        self.vaccine_shot_choice3_radio.config(bg="#FFFAFA")
        # Create choice 4
        self.vaccine_shot_choice4_radio = tk.Radiobutton(self, text="2nd Booster - fully vaccinated", font=("Arial", 8), variable=self.vaccine_shot_choice, value="4")
        self.vaccine_shot_choice4_radio.place(x=130, y=509)
        self.vaccine_shot_choice4_radio.config(bg="#FFFAFA")

        # Ask if the user have been tested for COVID-19. 
        self.covid_test_label = tk.Label(self, text="Have you been tested for COVID-19? ", width=41,  font=("Tekton Pro", 10, "bold"))
        self.covid_test_label.place(x=17, y=540)
        self.covid_test_label.config(bg="#FFFAFA")
         # Create the covid test choice variable
        self.covid_test_shot_choice = tk.StringVar()
        # Create choice 1
        self.covid_test_choice1_radio = tk.Radiobutton(self, text="Yes - Positive", font=("Arial", 8), variable=self.covid_test_shot_choice, value="1")
        self.covid_test_choice1_radio.place(x=30, y=566)
        self.covid_test_choice1_radio.config(bg="#FFFAFA")
        # Create choice 2
        self.covid_test_choice2_radio = tk.Radiobutton(self, text="Yes - Pending", font=("Arial", 8), variable=self.covid_test_shot_choice, value="2")
        self.covid_test_choice2_radio.place(x=30, y=593)
        self.covid_test_choice2_radio.config(bg="#FFFAFA")
        # Create choice 3
        self.covid_test_choice3_radio = tk.Radiobutton(self, text="Yes - Negative", font=("Arial", 8), variable=self.covid_test_shot_choice, value="3")
        self.covid_test_choice3_radio.place(x=150, y=566)
        self.covid_test_choice3_radio.config(bg="#FFFAFA")
        # Create choice 4
        self.covid_test_choice4_radio = tk.Radiobutton(self, text="No", font=("Arial", 8), variable=self.covid_test_shot_choice, value="4")
        self.covid_test_choice4_radio.place(x=150, y=593)
        self.covid_test_choice4_radio.config(bg="#FFFAFA")

    # Create Risk Assessment label
        self.risk_assessment_label = tk.Label(self, text=" RISK ASSESSMENT ", height=2, font=("Tahoma", 10, "bold"))
        self.risk_assessment_label.place(x=400, y=10)
        self.risk_assessment_label.config(bg="#FFE1FF")
        # Ask if the user experienced any of the following symptoms: fever, cough, shortness of breath, sore throat, loss of taste or smell, or body aches
        self.symptoms = tk.Label(self, text=" Have you experienced any of the following symptoms:", width=46, font=("Tekton Pro", 10, "bold"))
        self.symptoms.place(x=400, y=55)
        self.symptoms.config(bg="#FFFAFA")

        # Create the symptoms choice variable
        self.fever_choice = StringVar()
        self.cough_choice = StringVar()
        self.sore_throat_choice = StringVar()
        self.shortness_of_breath_choice = StringVar()
        self.diarrhea_choice = StringVar()
        self.body_aches_choice = StringVar()
        self.loss_of_taste_choice = StringVar()
        self.loss_of_smell_choice = StringVar()

        # Create fever checkbutton
        self.fever_checkbox = tk.Checkbutton(self, text="Fever", font=("Arial", 8), variable=self.fever_choice)
        self.fever_checkbox.place(x=420, y=80)
        self.fever_checkbox.config(bg="#FFFAFA")
        # Create cough checkbutton
        self.cough_checkbox = tk.Checkbutton(self, text="Cough", font=("Arial", 8), variable=self.cough_choice)
        self.cough_checkbox.place(x=420, y=107)
        self.cough_checkbox.config(bg="#FFFAFA")
        # Create sore throat checkbutton
        self.sore_throat_checkbox = tk.Checkbutton(self, text="Sore throat", font=("Arial", 8), variable=self.sore_throat_choice)
        self.sore_throat_checkbox.place(x=420, y=134)
        self.sore_throat_checkbox.config(bg="#FFFAFA")
        # Create shortness of breath checkbutton
        self.shortness_of_breath_checkbox = tk.Checkbutton(self, text="Breathing difficulty", font=("Arial", 8), variable=self.shortness_of_breath_choice)
        self.shortness_of_breath_checkbox.place(x=520, y=134)
        self.shortness_of_breath_checkbox.config(bg="#FFFAFA")
        # Create diarrhea checkbutton
        self.diarrhea_checkbox = tk.Checkbutton(self, text="Diarrhea", font=("Arial", 8), variable=self.diarrhea_choice)
        self.diarrhea_checkbox.place(x=520, y=80)
        self.diarrhea_checkbox.config(bg="#FFFAFA")
        # Create body aches checkbutton
        self.body_aches_checkbox = tk.Checkbutton(self, text="Body aches", font=("Arial", 8), variable=self.body_aches_choice)
        self.body_aches_checkbox.place(x=520, y=107)
        self.body_aches_checkbox.config(bg="#FFFAFA")
        # Create loss of taste checkbutton
        self.loss_of_taste_checkbox = tk.Checkbutton(self, text="Loss of taste", font=("Arial", 8), variable=self.loss_of_taste_choice)
        self.loss_of_taste_checkbox.place(x=650, y=80)
        self.loss_of_taste_checkbox.config(bg="#FFFAFA")
        # Create loss of smell checkbutton
        self.loss_of_smell_checkbox = tk.Checkbutton(self, text="Loss of smell", font=("Arial", 8), variable=self.loss_of_smell_choice)
        self.loss_of_smell_checkbox.place(x=650, y=107)
        self.loss_of_smell_checkbox.config(bg="#FFFAFA")

        # Ask if the user have been in close contact with someone who has tested positive for COVID-19.
        self.close_contact = tk.Label(self, text=" Have you recently encountered a COVID-19 carrier?", width=46, font=("Tekton Pro", 10, "bold"))
        self.close_contact.place(x=400, y=165)
        self.close_contact.config(bg="#FFFAFA")
        # Create the close contact choice variable
        self.close_contact_choice = tk.StringVar()
        # Create Yes Radiobuttons
        self.close_contact_yes_radio = tk.Radiobutton(self, text="Yes", font=("Arial", 8), variable=self.close_contact_choice, value="yes")
        self.close_contact_yes_radio.place(x=420, y=190)
        self.close_contact_yes_radio.config(bg="#FFFAFA")
        # Create No Radiobuttons
        self.close_contact_no_radio = tk.Radiobutton(self, text="No", font=("Arial", 8), variable=self.close_contact_choice, value="no")
        self.close_contact_no_radio.place(x=570, y=190)
        self.close_contact_no_radio.config(bg="#FFFAFA")

    # Create Travel History label
        self.travel_history_label = tk.Label(self, text=" TRAVEL HISTORY ", height=2, font=("Tahoma", 10, "bold"))
        self.travel_history_label.place(x=400, y=240)
        self.travel_history_label.config(bg="#FFE1FF")
        # Ask if the user have traveled to any high-risk areas recently.
        self.high_risk_areas = tk.Label(self, text=" Have you traveled to any high-risk areas recently?", width=46, font=("Tekton Pro", 10, "bold"))
        self.high_risk_areas.place(x=400, y=285)
        self.high_risk_areas.config(bg="#FFFAFA")
        # Create the high risk areas choice variable
        self.high_risk_areas_choice = tk.StringVar()
        # Create Yes Radiobuttons
        self.high_risk_areas_yes_radio = tk.Radiobutton(self, text="Yes", font=("Arial", 8), variable=self.high_risk_areas_choice, value="yes")
        self.high_risk_areas_yes_radio.place(x=420, y=310)
        self.high_risk_areas_yes_radio.config(bg="#FFFAFA")
        # Create No Radiobuttons
        self.high_risk_areas_no_radio = tk.Radiobutton(self, text="No", font=("Arial", 8), variable=self.high_risk_areas_choice, value="no")
        self.high_risk_areas_no_radio.place(x=570, y=310)
        self.high_risk_areas_no_radio.config(bg="#FFFAFA")
        # Ask if the user have traveled internationally in the past 14 days.
        self.trav_internationally = tk.Label(self, text=" Have you traveled internationally in the past 14 days?", width=46, font=("Tekton Pro", 10, "bold"))
        self.trav_internationally.place(x=400, y=340)
        self.trav_internationally.config(bg="#FFFAFA")
        # Create the trav internationally choice variable
        self.trav_internationally_choice = tk.StringVar()
        # Create Yes Radiobuttons
        self.trav_internationally_yes_radio = tk.Radiobutton(self, text="Yes", font=("Arial", 8), variable=self.trav_internationally_choice, value="yes")
        self.trav_internationally_yes_radio.place(x=420, y=365)
        self.trav_internationally_yes_radio.config(bg="#FFFAFA")
        # Create No Radiobuttons
        self.trav_internationally_no_radio = tk.Radiobutton(self, text="No", font=("Arial", 8), variable=self.trav_internationally_choice, value="no")
        self.trav_internationally_no_radio.place(x=570, y=365)
        self.trav_internationally_no_radio.config(bg="#FFFAFA")
        # Ask if the user have recently attended large gatherings or events.
        self.large_event = tk.Label(self, text=" Have you recently been to a large gathering or an event?", width=46, font=("Tekton Pro", 10, "bold"))
        self.large_event.place(x=400, y=395)
        self.large_event.config(bg="#FFFAFA")
        # Create the trav internationally choice variable
        self.large_event_choice = tk.StringVar(value="no")
        # Create Yes Radiobuttons
        self.large_event_yes_radio = tk.Radiobutton(self, text="Yes", font=("Arial", 8), variable=self.large_event_choice, value="yes")
        self.large_event_yes_radio.place(x=420, y=420)
        self.large_event_yes_radio.config(bg="#FFFAFA")
        # Create No Radiobuttons
        self.large_event_no_radio = tk.Radiobutton(self, text="No", font=("Arial", 8), variable=self.large_event_choice, value="no")
        self.large_event_no_radio.place(x=570, y=420)
        self.large_event_no_radio.config(bg="#FFFAFA")

        # Create Submit Button
        submit_button = tk.Button(self, text="SAVE & SUBMIT", command= self.submit_data, bg="#FFE1FF", height=2)
        submit_button.place(x=730, y=595)
    
    # Define the data for submit
    def submit_data(self):
        # Get the entered data for Personal Information
        user_name = self.name_entry.get()
        user_age = self.age_entry.get()
        user_sex = self.gender_entry.get()
        user_resid_address = self.residential_address_entry.get()

        # Get the entered data for Contact Information
        user_contact_num = self.contact_num_entry.get()
        user_email_address = self.email_add_entry.get()

        # Get the entered data for Emergency Information
        emergency_name = self.guardian_name_entry.get()
        emergency_relationship = self.guardian_relationship_entry.get()
        emergency_contact_num = self.guardian_contact_entry.get()
        emergency_email = self.guardian_email_add_entry.get()

        # Get the entered data for Health Declaration
        vaccine = self.vaccine_shot_choice.get()
        tested = self.covid_test_shot_choice.get()

        # Get the entered data for Risk Assessment
        symptoms_fever = self.fever_choice.get()
        symptoms_cough = self.cough_choice.get()
        symptoms_sore_throat = self.sore_throat_choice.get()
        symptoms_shortness_of_breath = self.shortness_of_breath_choice.get()
        symptoms_diarrhea = self.diarrhea_choice.get()
        symptoms_body_aches = self.body_aches_choice.get()
        symptoms_loss_of_taste = self.loss_of_taste_choice.get()
        symptoms_loss_of_smell = self.loss_of_smell_choice.get()
        close_contact = self.close_contact_choice.get()

        # Get the entered data for Travel History
        high_risk = self.high_risk_areas_choice.get()
        travel = self.trav_internationally_choice.get()
        large_event = self.large_event_choice.get()

        # Save the file using CVS
        with open('entry.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([user_name, user_age, user_sex, user_resid_address, user_contact_num, user_email_address, 
                             emergency_name, emergency_relationship, emergency_contact_num, emergency_email, vaccine, 
                             tested, symptoms_fever, symptoms_cough, symptoms_sore_throat, symptoms_shortness_of_breath,
                             symptoms_diarrhea, symptoms_body_aches, symptoms_loss_of_taste, symptoms_loss_of_smell,
                             close_contact, high_risk, travel, large_event])
            # Create notification for user
            if travel == "No" and high_risk == "No" and large_event == "No":
                # Display that you are not a close contact and not a covid positive
                window4 = NotifyFrame(self.master)
            else:
                # Display that you are not a close contact and not a covid positive
                window4 = NotifyFrame(self.master)

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
