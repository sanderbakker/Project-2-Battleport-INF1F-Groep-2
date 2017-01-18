"""Module containing ship classes"""


class MainShip:
    """Main class containing the base values & methods"""
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.size = 0
        self.health = 0

    def damage(self):
        """Lowers health by 1"""
        self.health -= 1

    def placement(self):
        """Allows for placement on the grid"""
        pass

    def turn(self):
        """Turns ship 180 degrees, allowing for offensive and defensive positioning"""
        self.x = self.x - 1
        self.y = self.y


class Saltire(MainShip):
    """Furgo Saltire & Santa Bettina class."""
    def __init__(self, name, x, y):
        self.name = name
        self.x = y
        self.y = y
        self.health = 2
        self.size = 2


class Windsurf(MainShip):
    """Silver Whisper, Windsurf, Sea Spirit & Intensity class"""
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.health = 3
        self.size = 3


class Amadea(MainShip):
    """Amadea & Merapi class"""
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.health = 4
        self.size = 4
