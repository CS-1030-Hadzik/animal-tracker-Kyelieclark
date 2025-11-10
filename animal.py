class Animal:
    """
    Base class representing a generic animal.
    """
    # Class-level attribute
    kingdom = "Animalia"
    # TODO create a class-level attribute that is a list of all the Animal objects
    

    def __init__(self, name, species):
        self.name = name
        self.species = species


    def speak(self):
        print("The animal makes a noise.")

    def __str__(self):
        return f"kingdom:{self.kingdom}, Name: {self.name} species:{self.species}"
   