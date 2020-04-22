import pyttsx3
from gtts import gTTS
import playsound
import os
from datetime import datetime

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 130)

def speak1(text):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.runAndWait()

def speak2(text):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

def speak3(text):
    tts = gTTS(text=text, lang="en-us")
    hasil_suara = "audio.mp3"
    tts.save(hasil_suara)
    playsound.playsound(hasil_suara)
    os.remove(hasil_suara)

def speak4(text):
    tts = gTTS(text=text, lang="en-ca")
    hasil_suara = "audio.mp3"
    tts.save(hasil_suara)
    playsound.playsound(hasil_suara)
    os.remove(hasil_suara)

def speak5(text):
    tts = gTTS(text=text, lang="en-uk")
    hasil_suara = "audio.mp3"
    tts.save(hasil_suara)
    playsound.playsound(hasil_suara)
    os.remove(hasil_suara)

def speak6(text):
    tts = gTTS(text=text, lang="en-gb")
    hasil_suara = "audio.mp3"
    tts.save(hasil_suara)
    playsound.playsound(hasil_suara)
    os.remove(hasil_suara)

def speak7(text):
    tts = gTTS(text=text, lang="en-au")
    hasil_suara = "audio.mp3"
    tts.save(hasil_suara)
    playsound.playsound(hasil_suara)
    os.remove(hasil_suara)

def speak8(text):
    tts = gTTS(text=text, lang="en-in")
    hasil_suara = "audio.mp3"
    tts.save(hasil_suara)
    playsound.playsound(hasil_suara)
    os.remove(hasil_suara)

def speak9(text):
    tts = gTTS(text=text, lang="en-ph")
    hasil_suara = "audio.mp3"
    tts.save(hasil_suara)
    playsound.playsound(hasil_suara)
    os.remove(hasil_suara)

def speak10(text):
    tts = gTTS(text=text, lang="en-nz")
    hasil_suara = "audio.mp3"
    tts.save(hasil_suara)
    playsound.playsound(hasil_suara)
    os.remove(hasil_suara)

def time():
    hour = int(datetime.now().hour)
    if hour >= 5 and hour <= 10:
        speak2("Good Morning")
    elif hour >= 11 and hour <= 14:
        speak2("Good Afternoon")
    elif hour >= 15 and hour <= 19:
        speak1("Good Evening, Sir")
    else:
        speak2("Good Night")

# time()
