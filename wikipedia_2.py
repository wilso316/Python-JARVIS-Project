"""
    Name: wikipedia_2.py
    Author: Maya Wilson
    Created: 3/21/23
    Purpose: Use wikipedia module to print infomation in OOP

"""

# pip install wikipedia
import wikipedia

class WikipediaApp:
    def __init__(self):
        pass

    def get_wikipedia(self):
        """
            Search Wikipedia
        """
        try:
            # Type in your search term
            result = input("Search Wikipedia: ")
            # Return a summary result of 3 sentences
            self.__summary = wikipedia.summary(result, sentences=3)

        except:
            # use raise for troubleshooting exceptions
            # raise
            # If there is an exception, allow the user to try again.
            print("Try a different search term.")

    def display_wikipedia(self):
        """
            Display Wikipedia search results

        """
        print(self.__summary)

# Create a jarvis program object
wikipedia_app = WikipediaApp()
while True:
    wikipedia_app.get_wikipedia
    wikipedia_app.display_wikipedia()