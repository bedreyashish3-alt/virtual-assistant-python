import speech_recognition as sr
import pyttsx3
import wikipedia
import pywhatkit
import pyjokes
import webbrowser
import datetime
import os

from config import *

# ----------------------------
# Initialize Speech Engine
# ----------------------------

engine = pyttsx3.init()

voices = engine.getProperty("voices")

engine.setProperty("voice", voices[1].id)

engine.setProperty("rate", VOICE_RATE)

engine.setProperty("volume", VOICE_VOLUME)


# ----------------------------
# Speak Function
# ----------------------------

def speak(text):
    print(f"{ASSISTANT_NAME}: {text}")
    engine.say(text)
    engine.runAndWait()


# ----------------------------
# Greeting
# ----------------------------

def wish():

    hour = datetime.datetime.now().hour

    if hour < 12:
        speak("Good Morning")

    elif hour < 18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak(f"I am {ASSISTANT_NAME}. How can I help you?")


# ----------------------------
# Listen
# ----------------------------


def listen():
    
    recognizer = sr.Recognizer()

    recognizer.energy_threshold = 300
    recognizer.pause_threshold = 0.8

    print("\nAvailable Microphones:")

    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print(index, "-", name)

    mic = int(input("\nEnter microphone number: "))

    with sr.Microphone(device_index=mic) as source:

        print("\nSpeak now...")

        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=6
            )

        except sr.WaitTimeoutError:

            print("No speech detected.")

            return ""

    try:

        print("Recognizing...")

        query = recognizer.recognize_google(audio)

        print("You said:", query)

        return query.lower()

    except Exception as e:

        print(e)

        return ""
# ----------------------------
# Wikipedia
# ----------------------------

def wikipedia_search(query):

    query = query.replace("wikipedia", "")

    result = wikipedia.summary(query, sentences=WIKIPEDIA_SENTENCES)

    speak(result)


# ----------------------------
# Google Search
# ----------------------------

def google_search(query):

    search = query.replace("search", "")

    url = "https://www.google.com/search?q=" + search

    webbrowser.open(url)

    speak("Searching Google")


# ----------------------------
# Play Song
# ----------------------------

def play_song(query):

    song = query.replace("play", "")

    speak("Playing " + song)

    pywhatkit.playonyt(song)


# ----------------------------
# Joke
# ----------------------------

def tell_joke():

    joke = pyjokes.get_joke()

    speak(joke)


# ----------------------------
# Time
# ----------------------------

def tell_time():

    current = datetime.datetime.now().strftime("%I:%M %p")

    speak("Current time is " + current)


# ----------------------------
# Date
# ----------------------------

def tell_date():

    today = datetime.datetime.now().strftime("%d %B %Y")

    speak("Today's date is " + today)


# ----------------------------
# Open Websites
# ----------------------------

def open_google():

    webbrowser.open(GOOGLE_URL)

    speak("Opening Google")


def open_youtube():

    webbrowser.open(YOUTUBE_URL)

    speak("Opening YouTube")


def open_gmail():

    webbrowser.open(GMAIL_URL)

    speak("Opening Gmail")


def open_instagram():

    webbrowser.open(INSTAGRAM_URL)

    speak("Opening Instagram")


# ----------------------------
# Google Maps
# ----------------------------

def open_map(query):

    place = query.replace("map", "")

    webbrowser.open(MAP_URL + place)

    speak("Opening map")


# ----------------------------
# Shutdown
# ----------------------------

def shutdown():

    speak("Shutting down your computer")

    os.system("shutdown /s /t 5")