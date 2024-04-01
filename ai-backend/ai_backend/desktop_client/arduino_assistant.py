import speech_recognition as sr
from gtts import gTTS
import playsound
import requests
import os

url = "https://fantastic-couscous-49wgvjq9645hjg44-5000.app.github.dev/"

recognizer = sr.Recognizer()

def req_query(query):
    if "weather" in query:
        data = {"action":"getWeather","query":query}
        x = requests.post(url,json=data)
        return str(x.text)
    else:
        data = {"action":"general","query":query}
        x = requests.post(url,json=data)
        return str(x.text)

def rec_audio():
    with sr.Microphone() as s:
        print("recording...")
        audio = recognizer.listen(s)
    return audio

def play_res(text):
    tts = gTTS(text=text,lang="en")
    tts.save("temp.mp3")
    playsound.playsound("temp.mp3")
    os.remove("temp.mp3")

def recognize(audio):
    try:
        text = recognizer.recognize_google(audio)
        print(text)
        return text
    except sr.UnknownValueError:
        print("Unknown VALUE Error")
    except sr.RequestError:
        print("Service Inaccessible")

def get_user_query():
    print("Microphone Button Clicked!")
    try:
        query = rec_audio()
        text = recognize(query)
        res = req_query(text)
        play_res(res)
    except ConnectionError:
        message_box = customtkinter.CTkMessageBox(self, title="No Internet Connection", message="Please Check Your Internet Connection")
        message_box.show()
