#---Base Class: Animal 
class Animal: 
    """A base class for animals"""

    def __init__(self, name, species):
        self.name = name
        self.species = species
        print(f"An Animal object ({self.species}) named {self.name} was created.")

    #Method of the Animal class
    def make_sound(self):
        """Generic method for making a sound """
        print("Some generic animal sound.")

    # Another method
    def display_info(self):
        """Display basic information about the animal"""
        print(f"Name: {self.name}, Species: {self.species}")


# --- Derived Class: Dog (inherits from Animal) ---
class Dog(Animal):
    """A derived class for dogs, inheriting from Animal"""

    def __init__(self, name, breed):
        # Call the constructor of the base class (Animal)
        super().__init__(name, species="Dog")
        self.breed = breed
        print(f"A Dog Object ({self.breed}) named {self.name} was created.")

    # Override the make_sound method for dogs
    def bark(self):
        """Makes the dog bark. """
        print("Woof! Woof!")

    # Override the make_sound method from the parent class (Polymorphism)
    def make_sound(self):
        """Makes the dog bark (specific sound). """
        self.bark()

    def display_info(self):
        """Display information about the dog."""
        super().display_info()
        print(f"Bread: {self.breed}")

#---Derived Class: Cat (inherits from Animal)---
class Cat(Animal):
    """A derived class for cats, inheriting from Animal"""
    
    def __init__(self, name, color):
        #Call the constructor of the base class (Animal)
        super().__init__(name, species="Cat")
        self.color = color
        print(f"A Cat object ({self.color}) named {self.name} was created.")

    def meow(self):
        """Makes the cat meow. """
        print("Meow! Meow!")

    def make_sound(self):
        """Makes the cat meow (specific sound). """
        self.meow()

    def display_info(self):
        """Display Information about the cat."""
        super().display_info()
        print(f"Color: {self.color}")

#--- Creating Objects (Instances) and Using Them---
print("\n--- Creating Objects ---")

my_dog = Dog("Buddy", "Golden Retriever")
my_cat = Cat("Whiskers", "Tabby")

print("\n--- Using Objects ---")
print(f"My Dog's name is: {my_dog.name}")
print(f"My Cat's name is: {my_cat.name}")

#calling methods
my_dog.bark()
my_cat.meow()

#call methods inherited from the animal class
my_dog.display_info()
my_cat.display_info()

#Demostrate polymorphism: calling the same method name on different objects
print("\n---Demostrating Polymorphism---")
my_dog.make_sound()
my_cat.make_sound()