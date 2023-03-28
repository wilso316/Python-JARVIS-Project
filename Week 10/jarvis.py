"""
    Name: wiki_jarvis.py
    Author: Maya Wilson
    Created: 3/21/23
    Purpose: Use wikipedia module to print infomation in OOP and use Text-to-Speech and Speech Recognition to print Wikipedia
    This program uses wikipedia_class module

"""
# Install/import pytts3, wiki, speech recognition
import speech_recognition as sr
import pyttsx3
import wikipedia_class
from time import sleep

# Create class Jarvis
class Jarvis:
    def __init__(self) -> None: 
        # Create SpeechRecognition recognizer object
        self.r = sr.Recognizer()

        # Create constants for speech engine
        RATE = 175  # integer default: 200 words per minute
        VOLUME = .7 # float default: 1.0, range: 0.0-1.0 inclusive
        VOICE =1    # integer default: 0 for David (male), set 1 for Zira (female)

        # Initialize the pyttxs3 voice engine
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', RATE)
        self.engine.setProperty('volume', VOLUME)

        # Retrieves all available voices from your system
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[VOICE].id)
        # Run engine to set properties
        self.engine.runAndWait()
    
    def user_input(self):
        """ Recognizes user voice input using
            Speech Recognition module, converts it to text
        """
        # Your local microphone as the source
        with sr.Microphone() as source:
            print("Listening . . .")
            self.r.pause_threshold = 1
            # Start listening for speech
            audio = self.r.listen(source)
            try:
                print("Recognizing . . . ")
                # Capture the recognized word in a string variable
                recognized_words = self.r.recognize_google(
                    audio, language='en-US', show_all=True)
                # Google Speech Recognition returns a list of dictionaries
                # Pull only the transcript with the highest confidence
                self.query = recognized_words['alternative'][0]['transcript']
                print(self.query)

            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                # If there was an error communication with Google Speech
                print(f"Google Speech did not responds: {e}")
    
    def wiki_search(self):
        # Get self.query and use wikipedia class to search up term
        wiki = wikipedia_class.WikipediaApp()
        # Call method to get_wiki_summary
        summary = wiki.get_wikipedia(self.query)
        print(summary)
        self.engine.say(summary)
        sleep(3)

    def greet_user(self):
        print("Hello I am JARVIS. Your personal AI assistant.")
        self.engine.say("Hello I am JARVIS. Your personal AI assistant.")
        self.engine.runAndWait()

    def voice_commands(self):
        # If you say quit, the program will exit
        if self.query == "quit":
            print("Goodbye!")
            exit()

# ----------------------------- MAIN PROGRAM -----------------------------------#
# Create a jarvis program object
jarvis = Jarvis()
jarvis.greet_user()
while True:
    jarvis.user_input()
    jarvis.wiki_search()
    jarvis.voice_commands()