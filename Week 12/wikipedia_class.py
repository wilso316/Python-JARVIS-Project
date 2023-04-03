"""
    Name: wikipedia_class.py
    Author: Maya Wilson
    Created: 3/21/23
    Purpose: Use wikipedia module to print infomation in OOP

"""

# pip install wikipedia
import wikipedia

class WikipediaApp:
    def __init__(self):
        pass

    def get_wikipedia(self, query):
        """
            Search Wikipedia
        """
        try:
            # Return a summary result of 3 sentences
            self.__summary = wikipedia.summary(query, sentences=3)
            return self.__summary

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
