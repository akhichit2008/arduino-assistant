import tkinter as tk
from PIL import Image, ImageTk
from arduino_assistant import get_user_query
import threading


def clickbutton():
    net_thread = threading.Thread(target=get_user_query)
    net_thread.start()
    net_thread.join()

    
class AssistantUIDesktop(tk.Frame):
  def __init__(self, master):
    super().__init__(master)

    # Create a canvas to draw on (optional)
    self.canvas = tk.Canvas(self, width=200, height=100)
    self.canvas.pack()
    #customtkinter.set_appearance_mode("Dark")
    mic_image = Image.open("microphone.jpg")  # Replace with your microphone image path
    mic_image = mic_image.resize((30, 30), Image.Resampling.LANCZOS)  # Use Resampling.LANCZOS
    self.mic_icon = ImageTk.PhotoImage(mic_image)

    # Create a button with microphone icon
    self.button = tk.Button(self.master, image=self.mic_icon, command=clickbutton)
    self.button.pack()

    # Configure window appearance (optional)
    self.configure(background="gray80")  # Set background color (optional)

    # Remove maximize and minimize buttons
    self.master.attributes('-toolwindow', True)  # Alternative approach

    # Keep the title bar with only close button
    self.master.title("Fancy UI")  # Set window title (optional)

    # Position the UI in the desired location
    self.master.geometry("200x100+"+str(self.master.winfo_screenwidth() - 300)+"+50")


def init_ui():
  root = tk.Tk()
  ui = AssistantUIDesktop(root)
  ui.mainloop()
  ui_thread.stop()
  net_thread.stop()

ui_thread = threading.Thread(target=init_ui)

if __name__ == "__main__":
    ui_thread.start()
    ui_thread.join()
