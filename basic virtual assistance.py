import speech_recognition as sr
import webbrowser  
import pyaudio
import pyttsx3
import os
import pygame
import requests
from openai import OpenAI
import urllib.parse
# import kiye humne joh module necessary the

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

# def aiProcess(command):
#     client = OpenAI(api_key="sk-proj-ScpdMEyVikVzY5rJBqmtT3BlbkFJmubAoD0K56D9gNpTdVZJ",
#     )

#     completion = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
#         {"role": "user", "content": command}
#     ]
#     )

#     return completion.choices[0].message.content



def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open spotify" in c.lower():
        webbrowser.open("https://spotify.com")
    if "play" in c.lower():
            parts = c.lower().split("play", 1)  # Split at "play"
            if len(parts) > 1:
                song_name = parts[1].strip().strip('"')  # Remove surrounding quotes if any
                search_query = urllib.parse.quote(song_name)
                search_url = f"https://www.youtube.com/results?search_query={search_query}"
                webbrowser.open(search_url)
                speak_old(f"Playing {song_name} on YouTube.")
            else:
                speak_old("Sorry, I didn't understand the search query.")    
    elif "search" in c:
        parts = c.split("search", 1)  # Split at "search"
        if len(parts) > 1:
            search_query = parts[1].strip().strip('"')  # Remove surrounding quotes if any
            search_query_encoded = urllib.parse.quote(search_query)
            search_url = f"https://www.google.com/search?q={search_query_encoded}"
            webbrowser.open(search_url)
            speak_old(f"Searching for {search_query} on Google.")
        else:
            speak_old("Sorry, I didn't understand the search query.")

    elif "turn" in c:
        parts = c.split("turn", 1)  # Split at "search"
        if len(parts) > 1:
            search_anysong = parts[1].strip().strip('"')  # Remove surrounding quotes if any
            search_anysong_spotify = urllib.parse.quote(search_anysong)
            search_url = f"https://open.spotify.com/search/{search_anysong_spotify}"
            webbrowser.open(search_url)
            speak_old(f"Searching for {search_anysong} on spotify.")
        else:
            speak_old("Sorry, I didn't understand the search query.")

    elif "off" in c:
        speak_old("thank you, please feel free to ask anything next time.")
       
        
     
if __name__ == "__main__":
    speak_old("Initializing Jarvis....")# so yaha se code actually starts 
    while True:
        print("recognizing...")
        try:
            # toh hamara first voice input is piece of code se hoga
            with sr.Microphone() as source:
                print("Listening....")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=2)
            
            word = recognizer.recognize_google(audio)
            if word.lower() == "jarvis":
                speak_old("Yes?")
                #only work if you have said the wake word "jarvis"
                with sr.Microphone() as source:
                    print("Jarvis active....")
                    audio = recognizer.listen(source, timeout=2, phrase_time_limit=3)
                    command = recognizer.recognize_google(audio)

                    processCommand(command)# goes in the func

        except sr.UnknownValueError:
            print("Could not understand the audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except Exception as e:
            print(f"Error; {e}")