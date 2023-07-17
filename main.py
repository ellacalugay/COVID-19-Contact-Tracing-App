# Ella Lureen C. Calugay | BSCPE 1-5 | Final Project

# Pseudocode
# Import the UserInformation class from user_information.py
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

# Call the main function
main()