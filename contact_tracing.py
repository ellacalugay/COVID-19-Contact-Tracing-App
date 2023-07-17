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
            response = input("Have you been vaccinated for COVID-19? (yes/no)")
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

# Ask the user about Risk Assessment.
# Ask the user for his/her travel history.
# Ask the user about contact log.
# Ask the user about testing and test results for COVID 19.
# Ask the user about his/her emergency information.
# Ash the user if he/she wants to receive notifications from the app.