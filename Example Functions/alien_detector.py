"""
    Name: alien_detector.py
    Author: Maya Wilson
    Created: 3/8/23
    Purpose: Create alien objects
    Import modules
    Create objects
    Give attributes
    Print objects
    Print methods

"""
import jupitarian
import martian
from rich.progress import track
from rich.console import Console
from rich import print
from time import sleep

console = Console()

def detecting():
    sleep(.04)

console.print("| . . . . . Detecting Aliens . . . . . |", style="bold blue")
for x in track(range(100), description='[green]Detecting'):
    detecting()

console.print("| . . . . . LIFEFORM FOUND . . . . . . |", style="bold green")
sleep(2)

martian1 = martian.martian(2, "red", 5, 2)
jupitarian1 = jupitarian.jupitarian(4, "green", 7, 8)

print(martian1)
print(f"Is a martian an alien? {martian1.detector()}")

console.print("| . . . . . Detecting Aliens . . . . . |", style="bold blue")
for x in track(range(100), description='[green]Detecting'):
    detecting()

console.print("| . . . . . LIFEFORM FOUND . . . . . . |", style="bold green")
sleep(2)

print(jupitarian1)
print(f"Is a jupitarian an alien? {jupitarian1.detector()}")

