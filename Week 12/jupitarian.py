"""
    Name: jupitarian.py
    Author: Maya Wilson
    Created: 3/8/23
    Purpose: Create a Martian class that descends from alien parent class
    Pseudo: Import alien module
    Create child class
    Create two more attributes (fingers) with properties

"""
import alien
class jupitarian(alien.Alien):
    def __init__(self, antennae: int, color: str, arms: int, fingers: int):

        # Call parent class constructor
        super().__init__(antennae, color, arms)
        # Add attributes
        self._fingers = fingers

    def __str__(self) -> str:
        description = f"Alien is {self._color}, has {self._antennae} antennae and {self.arms} arms.\nThe jupitarian has {self._fingers} fingers."
        return description
    # Property based getter and setter
    @property
    def fingers(self):
        return self._fingers
    
    @fingers.setter
    def fingers(self, fingers):
        self._fingers = fingers
    
    