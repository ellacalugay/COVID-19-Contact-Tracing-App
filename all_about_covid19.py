# Ella Lureen C. Calugay | BSCPE 1-5 | Final Project

# Pseudocode
# Import necessary modules
import tkinter as tk
from PIL import ImageTk, Image

# Create a class for add entry
class AllAboutCovid(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        
        # Load and display the background image in the AddEntry frame
        self.add_image_path = "F:\\2nd sem\\OOP\\FINAL PROJ\\covid.png"
        self.add_original_image = Image.open(self.add_image_path)
        self.add_resized_image = self.add_original_image.resize((850, 650))
        self.background_image = ImageTk.PhotoImage(self.add_resized_image)

        canvas = tk.Canvas(self, width=850, height=650)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=self.background_image, anchor="nw")

        # Add the text as a label widget
        text = """COVID-19, also known as the coronavirus disease 2019, is a highly contagious respiratory ailment caused by the SARS coronavirus 2 (SARS-CoV-2). The virus is thought to have originated in bats and was possibly transmitted to humans via an intermediate animal host, while more research is needed to identify its specific origin. COVID-19 spreads largely through respiratory droplets produced when an infected person coughs, sneezes, speaks, or breathes. It can also spread by contacting infected surfaces or objects and then touching the face, particularly the mouth, nose, or eyes.
\n COVID-19 symptoms can range greatly, ranging from moderate to severe. Fever, cough, and shortness of breath are common symptoms. Fatigue, muscle aches, loss of taste or smell, sore throat, and headache are all possible symptoms. Some people infected with the virus may be asymptomatic, which means they have no visible symptoms but can still spread the virus to others.
\n COVID-19 can be exceptionally severe and even fatal, especially in older people and those who have underlying health issues such as heart disease, diabetes, or weakened immune systems. The virus has had a large global health and economic impact, with countries employing various methods to restrict its spread, including social isolation, mask-wearing, and lockdowns.
\n Multiple vaccinations were produced and disseminated globally to combat the pandemic, with guaranteed effectiveness in preventing severe sickness and lowering transmission. Variants of the virus, however, continue to evolve, providing hurdles to current COVID-19 control efforts. As the situation progresses, health officials continue to monitor and respond to the epidemic in order to protect public health and minimize its impact on communities.
\n As the world unites in solidarity and resilience, we hold onto hope, knowing that together, we will overcome this global challenge and emerge stronger, brighter, and more connected than ever before."""

        text_label = tk.Label(self, text=text, wraplength=800, bg="light pink", font=('new times roman', 12), justify='left')
        text_label.place(x=25, y=120)

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