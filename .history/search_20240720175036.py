import os
import tempfile
import datetime
import requests
import pygame
from bs4 import BeautifulSoup
from gtts import gTTS
import speech_recognition as sr
import webbrowser as wb
import streamlit as st
import wikipedia
import wikipedia
def search(query):  # Google search
    if "google" in query:
        # Clean up the query to make it suitable for search
        query = query.replace("hey", "").replace("eva", "").replace("can you", "").replace("google", "").replace("why", "").replace("what", "").replace("when", "").replace("where", "").replace("how", "").replace("search", "").strip()
        
        if not query:
            st.write("Please provide a valid search query.")
            return
        
        st.write("Searching Google for:", query)
        try:
            # Perform Google search (in a separate context like CLI or browser)
            pw.search(query)  # Note: This might not work well with Streamlit
            
            # Perform Wikipedia search
            summary = wikipedia.summary(query, sentences=3)
            st.write("Wikipedia Summary:", summary)
        
        except ImportError as e:
            st.write(f"Error importing modules: {e}")
        except wikipedia.exceptions.DisambiguationError as e:
            st.write(f"Disambiguation Error: {e}")
        except wikipedia.exceptions.PageError as e:
            st.write(f"Page Error: {e}")
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
            st.write(result)
        except ImportError as e:
            st.write(f"Error importing Wikipedia module: {e}")
        except Exception as e:
            st.write("No page found on Wikipedia")

def tempsearch(query):  # Search for the temperature
    if "temperature" in query or "weather" in query:
        query = query.replace("what", "").replace("is", "")
        link = "https://www.google.com/search?q=" + query
        result = requests.get(link)
        data = BeautifulSoup(result.text, "html.parser")
        try:
            temp = data.find("div", class_="BNeawe").text
            st.write(temp)
        except AttributeError:
            st.write("Could not retrieve temperature information.")

def timesearch(query):  # Search for the current time
    if "time" in query:
        query = query.replace("what", "").replace("is", "").replace("the", "")
        time = datetime.datetime.now().strftime("%H:%M") 
        st.write(time)

def datesearch(query):  # Search for the current date
    if "date" in query:
        query = query.replace("what", "").replace("is", "").replace("the", "")
        date = datetime.datetime.now().strftime("%d:%m:%Y")

        st.write(date)

def searchwhat(query):  # Google search for specific questions
    if any(word in query for word in ["what", "why", "when", "where", "how", "who", "which"]):
        query = query.replace("hey", "").replace("eva", "").replace("can you", "").replace("google", "").replace("why", "").replace("what", "").replace("when", "").replace("where", "").replace("how", "").replace("is", "").replace("search", "")
        try:
            import wikipedia as wk
            result = wk.summary(query, sentences=3)

            st.write(result)
        except ImportError as e:
            st.write(f"Error importing Wikipedia module: {e}")
        except Exception as e:
            st.write(f"An error occurred: {e}")