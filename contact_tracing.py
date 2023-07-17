# Ella Lureen C. Calugay | BSCPE 1-5 | Final Project

# Pseudocode
# Create a class named User Information that encapsulates the functionalities for asking the user's personal information and related details.
class UserInformation:
    # Create a non-parametrized constructor
    def __init__(self):
        self.personal_information = {}
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
        
# Ask the user about Risk Assessment.
# Ask the user for his/her travel history.
# Ask the user about contact log.
# Ask the user about testing and test results for COVID 19.
# Ask the user about his/her emergency information.
# Ash the user if he/she wants to receive notifications from the app.