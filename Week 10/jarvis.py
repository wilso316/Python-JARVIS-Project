"""
    Name: wiki_jarvis.py
    Author: Maya Wilson
    Created: 3/21/23
    Purpose: Use wikipedia module to print infomation in OOP and use Text-to-Speech and Speech Recognition to print Wikipedia
    This uses it within the same module

"""
# Install/import pytts3, wiki, speech recognition
import speech_recognition as sr
import pyttsx3
import wikipedia
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
    
    def get_wikipedia(self):
        """
            Search Wikipedia
        """
        try:
            print("Use Wikipedia")
            print("What would you like to look up?")
            self.engine.say("What would you like to look up?")
            self.engine.runAndWait()

            self.user_input()

            # Return a summary result of 3 sentences
            summary = wikipedia.summary(self.query, sentences=3)
            print(f"\n{summary}")
            self.engine.say(summary)
            self.engine.runAndWait()
            self.display_menu()

        except:
            # use raise for troubleshooting exceptions
            # raise
            # If there is an exception, allow the user to try again.
            self.engine.say("Sorry, try a different search term.")
            print("Try a different search term.")
            self.display_menu()
            self.engine.runAndWait()

    def display_menu(self):
        print("----- JARVIS Menu -----")
        print("Please say a command: ")
        print("Commands: Wikipedia | Quit")

    def greet_user(self):
        print("Hello I am JARVIS. Your personal AI assistant.")
        self.engine.say("Hello I am JARVIS. Your personal AI assistant.")
        jarvis.display_menu()
        self.engine.runAndWait()

    def voice_commands(self):
        # If you say quit, the program will exit
        if self.query.lower() == "quit":
            print("Goodbye!")
            exit()
        elif self.query.lower() == "wikipedia":
            self.get_wikipedia()

# ----------------------------- MAIN PROGRAM -----------------------------------#
# Create a jarvis program object
jarvis = Jarvis()
jarvis.greet_user()
while True:
    jarvis.user_input()
    jarvis.voice_commands()