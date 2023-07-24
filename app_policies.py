# Ella Lureen C. Calugay | BSCPE 1-5 | Final Project

# Pseudocode
# Import necessary modules
import tkinter as tk
from PIL import ImageTk, Image

# Create a class for App Policies
class AppPolicies(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        
        # Load and display the background image in the App Policies frame
        self.add_image_path = "F:\\2nd sem\\OOP\\FINAL PROJ\\policy.png"
        self.add_original_image = Image.open(self.add_image_path)
        self.add_resized_image = self.add_original_image.resize((850, 650))
        self.background_image = ImageTk.PhotoImage(self.add_resized_image)

        canvas = tk.Canvas(self, width=850, height=650)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=self.background_image, anchor="nw")
        
        # Add the text as a label widget
        text = "The COVID Tracing App is designed to help track and manage information related to COVID-19 cases and exposure. To ensure the privacy and security of users' data and provide a reliable service, the following app policy will be implemented:"

        text_label = tk.Label(self, text=text, wraplength=805, bg="light pink", font=('new times roman', 10, "bold"), justify='left')
        text_label.place(x=25, y=112)

        # Add the text as a label widget
        text = """1. Data Privacy and Security:
        • The app will collect and store only the minimum necessary data required for contact tracing, such as name, contact details, and possible exposure locations.
        • User data will be securely encrypted and stored in a protected database to prevent unauthorized access.
        • Data will only be accessible to authorized personnel involved in contact tracing and public health response efforts.
        \n 2. Consent and Opt-In:
        • Users will be required to give explicit consent and opt-in to participate in the contact tracing program.
        \n 3. Anonymity and Confidentiality:
        •The app will use anonymized data whenever possible to protect user privacy.
        •Personal identifiers will be kept separate from exposure data to ensure confidentiality.
        \n 4. User Rights and Transparency:
        •Users have the right to access their own data stored by the app.
        •Transparent information about data collection, storage, and usage will be provided in the app's privacy policy."""

        text_label = tk.Label(self, text=text, wraplength=400, bg="light pink", font=('new times roman', 10), justify='left')
        text_label.place(x=20, y=160)

        # Add the text as a label widget
        text = """5. Information Accuracy:
        •Users are responsible for providing accurate and up-to-date information when using the app.
        •The app will include mechanisms for users to review and update their contact details if needed. 
        \n 6. Prohibited Use:
        •Any misuse of the app for malicious or unauthorized purposes is strictly prohibited.
        •Users found engaging in fraudulent activities will be subject to legal action.
        \n 7. User Education and Support:
        •The app will provide educational resources about COVID-19 and best practices for preventing transmission.
        •Users will have access to customer support for any questions or concerns related to the app.
        \n 8. Compliance with Regulations:
        •The app will comply with all applicable data protection and privacy laws and regulations. \
By using the COVID Tracing App, users agree to abide by these policies. The success of the app relies on the cooperation and responsible use of the service by all users."""
        
        text_label = tk.Label(self, text=text, wraplength=400, bg="light pink", font=('new times roman', 10), justify='left')
        text_label.place(x=435, y=160)

        # Buttons
        button_frame = tk.Frame(self, bg="light pink")
        button_frame.pack(side="bottom", fill="x")
        
        # Create an exit button
        ok_button = tk.Button(self, text="OK", command=self.close_window, bg='#CD5555', font=('new times roman', 12))
        ok_button.place(x=405, y=580)

        # Create a turn back button
        back_button = tk.Button(self, text='Back', command=self.go_to_main_window, bg='light pink', font=('new times roman', 12))
        back_button.place(x=775, y=595)

     # Define the exit window. This home window will exit the program
    def close_window(self):
        self.master.destroy()

    # Go back to the main window.
    def go_to_main_window(self):
        self.destroy()
        self.master.deiconify()  # This will show the main window again.
    
    # Go back to the main window.
    def open_main_window(self):
        app = self.FrontPage()
        app.main_window()
    
# End of code.