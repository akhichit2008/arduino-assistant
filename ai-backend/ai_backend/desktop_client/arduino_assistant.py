import speech_recognition as sr
from gtts import gTTS
import playsound
import requests

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

def recognize(audio):
    try:
        text = recognizer.recognize_google(audio)
        print(text)
        return text
    except sr.UnknownValueError:
        print("Unknown VALUE Error")
    except sr.RequestError:
        print("Service Inaccessible")

        
if __name__ == "__main__":
    #audio = rec_audio()
    #recognize(audio)
    try:
        audio = rec_audio()
        text = recognize(audio)
        res = req_query(text)
        play_res(res)
    except requests.ConnectionError:
        print("Network connection Error")
