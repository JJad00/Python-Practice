class Pet:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "makes a sound"

    def __str__(self):
        return f"{self.name} the {self.__class__.__name__} says {self.speak()}"
