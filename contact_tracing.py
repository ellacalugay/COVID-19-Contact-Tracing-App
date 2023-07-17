# Ella Lureen C. Calugay | BSCPE 1-5 | Final Project

# Pseudocode
# Create a class named User Information that encapsulates the functionalities for asking the user's personal information and related details.
class UserInformation:
    # Create a non-parametrized constructor
    def __init__(self):
        self.personal_information = {}
        self.vaccinated_covid = False
        self.health_declaration = {}
        self.risk_assessment = {}
        self.travel_history = []
        self.contact_log = []
        self.covid19_testing = {}
        self.emergency_information = {}
        self.receive_notifications = False

    # Ask the user for his/her personal information.
    def ask_personal_information(self):
        print("Please provide you personal information:")
        self.personal_information["name"] = input("What is your full name?: ")
        self.personal_information["age"] = int(input("How old are you?: "))
        self.personal_information["gender"] = input("What is your gender?: ")
        self.personal_information["phone number"] = input("What is your contact number?: ")
        self.personal_information["email address"] = input("What is your email address?: ")
        self.personal_information["residential address"] = input("What is your residential address?: ")
        self.personal_information["occupation"] = input("What is your current occupation?: ")

        # Prompt for COVID-19 vaccination
        while True:
            response = input("Have you been vaccinated for COVID-19? (yes/no): ")
            if response in ["yes", "no"]:
                self.vaccinated_covid = response == "yes"
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
    
    # Ask the user for his/her covid vaccine type.
    def ask_covid_vaccination_type(self):
        if self.personal_information.get("vaccinated_covid"):
            while True:
                vaccination_type = input("Please select the type of COVID-19 vaccination you received:\n"
                                         "1 - 1st shot COVID vaccine\n"
                                         "2 - 2nd shot COVID vaccine\n"
                                         "3 - 1st shot booster\n"
                                         "4 - 2nd shot booster\n"
                                         "Enter the corresponding number: ")
                if vaccination_type in ["1", "2", "3", "4"]:
                    self.personal_information["covid_vaccination_type"] = int(vaccination_type)
                    break
                else:
                    print("Invalid input. Please enter a valid option (1, 2, 3, or 4).")

    # Ask the user about health declaration.
    def ask_health_declaration(self):
        print("Health Declaration:")
        self.health_declaration["fever"] = input("Have you experienced fever in the last 14 days? (Yes/No): ").lower() == "yes"
        self.health_declaration["cough"] = input("Have you experienced a new or worsening cough in the last 14 days? (Yes/No): ").lower() == "yes"
        self.health_declaration["breathing_issues"] = input("Have you experienced any breathing issues in the last 14 days? (Yes/No): ").lower() == "yes"
        self.health_declaration["fatigue"] = input("Have you experienced feeling excessively tired in the last 14 days? (Yes/No): ").lower() == "yes"
        self.health_declaration["loss of state and smell"] = input("Have you experienced anosmia(loss of smell) or ageusia (loss of taste) in the last 14 days? (Yes/No): ").lower() == "yes"
        self.health_declaration["sore throat"] = input("Have you experienced pain or irritation in the throat in the last 14 days? (Yes/No): ").lower() == "yes"
        self.health_declaration["diarrhea"] = input("Have you experienced diarrhea in the last 14 days? (Yes/No): ").lower() == "yes"

    # Ask the user about Risk Assessment.
    def ask_risk_assessment(self):
        print("Risk Assessment:")
        self.risk_assessment["underlying_health_conditions"] = input("Do you have any underlying health conditions? (Yes/No): ").lower() == "yes"
        self.risk_assessment["close_contact_positive_cases"] = input("Have you been in close contact with someone who has tested positive for COVID-19? If yes, who are they? (Yes/No): ").lower() == "yes"
        self.risk_assessment["recent_travel_history"] = input("Have you traveled internationally in the last 14 days? (Yes/No): ").lower() == "yes"

    # Ask the user for his/her travel history.
    def ask_travel_history(self):
        print("Travel History:")
        num_trips = int(input("How many trips have you taken recently? "))
        for i in range(num_trips):
            self.travel_history.append(input(f"Trip {i+1}: "))
            
    # Ask the user about contact log.
    def ask_contact_log(self):
            print("Contact Log:")
            num_contacts = int(input("How many contacts do you want to log? "))
            for i in range(num_contacts):
                self.contact_log.append(input(f"Contact {i+1}: "))

    # Ask the user about testing and test results for COVID 19.
    def ask_covid19_testing(self):
        print("COVID-19 Testing:")
        self.covid19_testing["tested_positive"] = input("Have you tested positive for COVID-19? (Yes/No): ").lower() == "yes"
        if self.covid19_testing["tested_positive"]:
            self.covid19_testing["test_date"] = input("Date of the COVID-19 test: ")
            self.covid19_testing["result_date"] = input("Date of the test result: ")
            self.covid19_testing["test_result"] = input("Test result (Positive/Negative): ").lower() == "positive"

    # Ask the user about his/her emergency information.   
    def ask_emergency_information(self):
            print("Emergency Information:")
            self.emergency_information["emergency_contact"] = input("Emergency Contact Name: ")
            self.emergency_information["emergency_phone"] = input("Emergency Contact Phone number: ")
            self.emergency_information["blood_type"] = input("Your Blood Type: ")

    # Ask the user if he/she wants to receive notifications from the app.
    def ask_receive_notifications(self):
        response = input("Do you want to receive notifications from the app? (Yes/No): ").lower()
        self.receive_notifications = response == "yes"