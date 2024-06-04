import google.generativeai as genai
from dotenv import load_dotenv
import tkinter as tk
from PIL import ImageGrab
import uuid
import os
import json
import pyttsx3 as tts
import threading
import speech_recognition as sr

load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)
engine = tts.init()

vision = genai.GenerativeModel('gemini-pro-vision')

def speech():
    rec = sr.Recognizer()
    mic = sr.Microphone()
    print("Listening")
    with mic as source:
        rec.adjust_for_ambient_noise(source)
        audio = rec.listen(source)
        text = rec.recognize_google(audio)
        print("Recording Done...")
        return text

def call_model(prompt, screenshot):
    response = vision.generate_content([prompt, screenshot])
    engine.say(response.text)
    engine.runAndWait()

def on_send():
    #prompt = prompt_field.get()
    prompt = speech()
    screenshot = ImageGrab.grab()
    screenshot.save(f"screenshot-{uuid.uuid4().hex}.png")
    send_btn.config(state=tk.DISABLED)  # Disable the send button
    threading.Thread(target=call_model_thread, args=(prompt, screenshot)).start()

def call_model_thread(prompt, screenshot):
    call_model(prompt, screenshot)
    root.after(0, enable_send_btn)  # Schedule enable_send_btn to be called in the main thread

def enable_send_btn():
    send_btn.config(state=tk.NORMAL)  # Enable the send button

root = tk.Tk()
root.title("DARVIN ASSIST")

#prompt_field = tk.Entry(root, width=30)
#prompt_field.pack(pady=10)

send_btn = tk.Button(root, text="Ask", command=on_send)
send_btn.pack()

root.mainloop()
