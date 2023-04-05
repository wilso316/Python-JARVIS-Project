"""
    Name: martian.py
    Author: Maya Wilson
    Created: 3/8/23
    Purpose: Create a Martian class that descends from alien parent class
    Pseudo: Import alien module
    Create child class
    Create two more attributes (tongue) with properties

"""
import alien
class martian(alien.Alien):
    def __init__(self, antennae: int, color: str, arms: int, tongue: int):


        super().__init__(antennae, color, arms)
        # Add attributes
        self._tongue = tongue

        # Property based getter and setter
    def __str__(self) -> str:
        description = f"Alien is {self._color}, has {self._antennae} antennae and {self.arms} arms.\nThe Martian has {self._tongue} tongues."
        return description
    @property
    def tongue(self):
        return self._tongue
    
    @tongue.setter
    def tongue(self, tongue):
        self._tongue = tongue
    
