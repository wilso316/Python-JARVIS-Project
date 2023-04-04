"""
    Name: alien.py
    Author: Maya Wilson
    Created: 3/8/2023
    Purpose: Create an alien class with 3 attributes: 
    Pseudo: Create alien class
    Create constructor with (antennae, color, arms, ) default attributes
    Use override _str_ method (in place of display function)
    Create a detector method that detects alien or not

"""
class Alien:
    def __init__(self, antennae: int, color: str, arms: int):
        """Initalize private attributes"""
        self._antennae = antennae
        self._color = color
        self._arms = arms
    
    def __str__(self) -> str:
        """Override the class __str__ method"""
        description = f"Alien is {self._color}, has {self._antennae} antennae and {self.arms} arms."
        return description
    
    def detector(self) -> bool:
        """Is the lifeform an alien?"""
        is_alien = self._arms > 2
        return is_alien
    
    # Property based getter and setter
    @property
    def arms(self):
        return self._arms
    
    @arms.setter
    def arms(self, arms):
        self._arms = arms