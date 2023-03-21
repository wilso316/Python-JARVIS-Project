"""
    Name: wikipedia_1.py
    Author: Maya Wilson
    Created: 3/21/23
    Purpose: Use wikipedia module to print infomation

"""

# pip install wikipedia
import wikipedia

# Type in your search term (Be specific)
result = input("Search Wikipedia (Be specific please): ")

# Return a summary result of 3 sentences
summary = wikipedia.summary(result, sentences=3)

# Print result
print(summary)