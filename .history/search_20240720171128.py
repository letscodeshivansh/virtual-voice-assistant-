import os
import tempfile
import datetime
import requests
import pygame
from bs4 import BeautifulSoup
from gtts import gTTS
import speech_recognition as sr
import webbrowser as wb

def search(query):  # Google search
    if "google" in query:
        query = query.replace("hey", "").replace("eva", "").replace("can you", "").replace("google", "").replace("why", "").replace("what", "").replace("when", "").replace("where", "").replace("how", "").replace("search", "")
        st.write("so, I found this")
        try:
            import pywhatkit as pw
            result = pw.search(query)
            import wikipedia as wk
            summary = wk.summary(query, sentences=3)
            st.write(summary)

        except ImportError as e:
            st.write(f"Error importing modules: {e}")
        except Exception as e:
            st.write(f"An error occurred: {e}")

def youtubesearch(query):  # Search anything on YouTube
    if "youtube" in query:
        st.write("searching on youtube")
        query = query.replace("hey", "").replace("eva", "").replace("can you", "").replace("google", "").replace("search", "").replace("youtube", "").replace("video", "").replace("play", "").replace("on", "")
        web = "https://www.youtube.com/results?search_query=" + query
        wb.open(web)

def wikisearch(query):  # Wikipedia search
    if 'wikipedia' in query:
        query = query.replace("hey", "").replace("search", "").replace("wikipedia", "").replace("eva", "")
        try:
            import wikipedia as wk
            result = wk.summary(query, sentences=5)
            speak("results on wikipedia are...")
            print(result)
            speak(result)
        except ImportError as e:
            print(f"Error importing Wikipedia module: {e}")
        except Exception as e:
            print("No page found on Wikipedia")
            speak("No page found on Wikipedia")

def tempsearch(query):  # Search for the temperature
    if "temperature" in query or "weather" in query:
        query = query.replace("what", "").replace("is", "")
        link = "https://www.google.com/search?q=" + query
        result = requests.get(link)
        data = BeautifulSoup(result.text, "html.parser")
        try:
            temp = data.find("div", class_="BNeawe").text
            speak(query)
            speak(temp)
        except AttributeError:
            speak("Could not retrieve temperature information.")
            print("Could not retrieve temperature information.")

def timesearch(query):  # Search for the current time
    if "time" in query:
        query = query.replace("what", "").replace("is", "").replace("the", "")
        time = datetime.datetime.now().strftime("%H:%M")
        speak(time)
        print(time)

def datesearch(query):  # Search for the current date
    if "date" in query:
        query = query.replace("what", "").replace("is", "").replace("the", "")
        date = datetime.datetime.now().strftime("%d:%m:%Y")
        speak(date)
        print(date)

def searchwhat(query):  # Google search for specific questions
    if any(word in query for word in ["what", "why", "when", "where", "how", "who", "which"]):
        query = query.replace("hey", "").replace("eva", "").replace("can you", "").replace("google", "").replace("why", "").replace("what", "").replace("when", "").replace("where", "").replace("how", "").replace("is", "").replace("search", "")
        speak("so, I found this")
        try:
            import wikipedia as wk
            result = wk.summary(query, sentences=3)
            print(result)
            speak(result)
        except ImportError as e:
            print(f"Error importing Wikipedia module: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
