import customtkinter
from customtkinter import CTk
from PIL import Image, ImageTk
from arduino_assistant import get_user_query
import threading
from customtkinter import CTk, CTkButton, CTkFrame
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


#CTk._set_appearance_mode("Dark")  # Or "Dark"

def clickbutton():
    net_thread = threading.Thread(target=get_user_query)
    net_thread.start()
    net_thread.join()




class AssistantUIDesktop(CTk):
    def __init__(self):
        super().__init__()
        # Create a CTkFrame (optional)
        self.frame = CTkFrame(self)
        self.frame.pack(padx=10, pady=10)

        # Load microphone image
        mic_image = Image.open("microphone.jpg")  # Replace with your image path
        mic_image = mic_image.resize((30, 30), Image.Resampling.LANCZOS)
        self.mic_icon = ImageTk.PhotoImage(mic_image)

        # Create microphone button with CTkButton
        self.button = CTkButton(self.frame, image=self.mic_icon, command=clickbutton)
        self.button.pack()

         # Or "Dark" for dark mode

        # Set window title (optional)
        self.title("Fancy UI")

        # Position the window
        screen_width = self.winfo_screenwidth()
        self.geometry(f"200x100+{screen_width - 300}+50")

        # Set foreground color options (choose one or combine)
        # Option 1: Set foreground color for the entire window
        self.configure(fg="black")  # Replace with desired color

        # Option 2: Set foreground color for specific widgets
        # self.button.configure(fg="white")  # Set foreground color of the button



def init_ui():
    ui = AssistantUIDesktop()
    ui.mainloop()




if __name__ == "__main__":
    ui_thread = threading.Thread(target=init_ui)
    ui_thread.start()
    ui_thread.join()
