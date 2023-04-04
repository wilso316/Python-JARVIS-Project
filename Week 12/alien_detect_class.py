"""
    Name: alien_detect_class.py
    Author: Maya Wilson
    Created: 4/3/23
    Purpose: Alien Detector class

"""
import jupitarian
import martian
from rich.progress import track
from rich.console import Console
from rich import print
from time import sleep

class Alien_Detect:
    def __init__(self):
        self.console = Console()
        self.martian1 = martian.martian(2, "red", 5, 2)
        self.jupitarian1 = jupitarian.jupitarian(4, "green", 7, 8)   
    
    def detecting(self):
        self.console.print("| . . . . . Detecting Aliens . . . . . |", style="bold blue")
        for x in track(range(100), description='[green]Detecting'):
            sleep(.04)

        self.console.print("| . . . . . LIFEFORM FOUND . . . . . . |", style="bold green")
        sleep(2)

    
    def life_form1(self):
        return self.martian1
    
    def life_form2(self):
        return self.jupitarian1
        
        
        
            