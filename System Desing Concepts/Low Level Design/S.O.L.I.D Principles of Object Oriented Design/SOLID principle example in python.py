
# SOLID is an acronym that stands for five principles of object-oriented programming and design. These principles, when applied together, can make the code more maintainable, flexible, and less prone to bugs.

# Single Responsibility Principle (SRP) - A class should have only one reason to change, meaning it should have only one responsibility.
# Open-Closed Principle (OCP) - A class should be open for extension but closed for modification. This means that new functionality should be added by extending the class, not by modifying its existing code.
# Liskov Substitution Principle (LSP) - Subtypes should be substitutable for their base types. This means that objects of a derived class should be able to replace objects of the base class without affecting the correctness of the program.
# Interface Segregation Principle (ISP) - A class should not be forced to implement interfaces it does not use.
# Dependency Inversion Principle (DIP) - High-level modules should not depend on low-level modules, but both should depend on abstractions.

# By following these principles, code will be more readable, less complex, and easier to maintain.


# Here We are Going to Desing a Bird with SOLID principles will see the examples with SOLID Principles and Without SOLID Principles

# Single Responsibility Principle (SRP): The Bird class should have a single responsibility, which is to represent a bird.
# The Bird class has a single responsibility, which is to represent a bird.
# The BirdSound class is responsible for handling the sounds birds make, adhering to the SRP.
# The BirdMovement class is responsible for managing how birds move, adhering to the SRP.
# This separation ensures that each class has a distinct and single responsibility, making the design clean and maintainable.

# Adhering to SRP (Single Responsibility Principle)

class Bird:
    def __init__(self, name):
        self.name = name

class BirdSound:
    def make_sound(self, bird):
        pass

class BirdMovement:
    def move(self, bird):
        pass



# The Bird class has multiple responsibilities: making sounds and moving. This violates the SRP because it combines two distinct tasks in a single class.
# This violation can lead to difficulties in maintaining and extending the code, as changes related to one responsibility may inadvertently affect the other. It's also less modular and harder to understand than the design adhering to the SRP

# Violating SRP (Single Responsibility Principle)
class Bird:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass

    def move(self):
        pass






# Open-Closed Principle (OCP): The Bird class should be open for extension but closed for modification, allowing us to add new bird types without changing existing code.
# The Bird class is abstract and defines an abstract method describe, ensuring that all subclasses implement this method.
# Specific bird types (Sparrow, Penguin, and Ostrich) inherit from Bird and provide their own implementations of describe.
# This design adheres to the OCP by allowing for easy extension with new bird types (e.g., adding a Parrot) without modifying existing code.
# Adhering to OCP (Open-Closed Principle)
from abc import ABC, abstractmethod

class Bird(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def describe(self):
        pass

class Sparrow(Bird):
    def describe(self):
        return f"{self.name} is a sparrow."

class Penguin(Bird):
    def describe(self):
        return f"{self.name} is a penguin."

class Ostrich(Bird):
    def describe(self):
        return f"{self.name} is an ostrich."

# The Bird class has a single method describe that checks the species of the bird and provides a description based on the species.
# To add a new bird type, you would need to modify the existing describe method, violating the OCP by making the class open for modification.
# Violating OCP (Open-Closed Principle)
class Bird:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def describe(self):
        if self.species == "sparrow":
            return f"{self.name} is a sparrow."
        elif self.species == "penguin":
            return f"{self.name} is a penguin."
        elif self.species == "ostrich":
            return f"{self.name} is an ostrich."
        else:
            return f"{self.name} is an unknown bird."


# Liskov Substitution Principle (LSP): Subtypes (specific bird types) should be substitutable for their base type (Bird) without affecting program correctness.
# The Bird class defines a common method move.
# Specific bird types (Sparrow and Penguin) inherit from Bird and provide their own implementations of the move method.
# This adheres to the LSP because the derived classes can be substituted for the base class without affecting the correctness of the program.
# Adhering to LSP (Liskov Substitution Principle)
class Bird:
    def __init__(self, name):
        self.name = name

    def move(self):
        pass

class Sparrow(Bird):
    def move(self):
        return f"{self.name} is flying."

class Penguin(Bird):
    def move(self):
        return f"{self.name} is swimming."

# The Bird class's move method uses a condition to check the bird's ability and provide a description based on that ability.
# This violates the LSP because adding a new bird type with a different ability (e.g., "running") would require modifying the existing class.
# Violating LSP (Liskov Substitution Principle)
class Bird:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability

    def move(self):
        if self.ability == "flying":
            return f"{self.name} is flying."
        elif self.ability == "swimming":
            return f"{self.name} is swimming."




# Interface Segregation Principle (ISP): Clients should not be forced to depend on methods they don't use, so the Bird class should provide only the most essential methods.
# The Bird class represents the common properties of a bird.
# Specific bird types (Sparrow and Penguin) inherit from Bird and implement interfaces (Flyable and Swimmable) that specify the methods they support.
# Adhering to ISP (Interface Segregation Principle)
from abc import ABC, abstractmethod

class Bird(ABC):
    def __init__(self, name):
        self.name = name

class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass

class Swimmable(ABC):
    @abstractmethod
    def swim(self):
        pass

class Sparrow(Bird, Flyable):
    def fly(self):
        return f"{self.name} is flying."

class Penguin(Bird, Swimmable):
    def swim(self):
        return f"{self.name} is swimming."
    

# The Bird class defines a single method move for all bird types, which doesn't respect the ISP because it forces all clients to depend on this single method.
# Violating ISP (Interface Segregation Principle)
from abc import ABC, abstractmethod

class Bird(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def move(self):
        pass


# Dependency Inversion Principle (DIP): High-level modules (e.g., bird behaviors) should not depend on low-level modules. Both should depend on abstractions (interfaces).
# The Bird class defines the common method move.
# The BirdController class is responsible for controlling bird movements and depends on an abstraction (the Bird interface).
# Specific bird types (Sparrow and Penguin) implement the move method.
# Adhering to DIP (Dependency Inversion Principle)
from abc import ABC, abstractmethod

class Bird(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def move(self):
        pass

class BirdController:
    def __init__(self, bird):
        self.bird = bird

    def make_move(self):
        return self.bird.move()

class Sparrow(Bird):
    def move(self):
        return f"{self.name} is flying."

class Penguin(Bird):
    def move(self):
        return f"{self.name} is swimming."


# The Bird class directly handles bird movements, which violates the DIP as high-level modules (e.g., BirdController) still depend on low-level modules (specific bird types).
# Violating DIP (Dependency Inversion Principle)
class Bird:
    def __init__(self, name):
        self.name = name

    def move(self):
        pass

class BirdController:
    def __init__(self, bird):
        self.bird = bird

    def make_move(self):
        return self.bird.move()

class Sparrow(Bird):
    def move(self):
        return f"{self.name} is flying."

class Penguin(Bird):
    def move(self):
        return f"{self.name} is swimming."




#Example for Design a Bird with satisfies SOLID principles.
from abc import ABC, abstractmethod

# Interface for flyable birds
class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass

# Interface for singable birds
class Singable(ABC):
    @abstractmethod
    def sing(self):
        pass

# Base Bird class adhering to SRP and OCP
class Bird:
    def __init__(self, name):
        self.name = name

# Specific bird types adhering to LSP and ISP
class Sparrow(Bird, Flyable, Singable):
    def fly(self):
        return f"{self.name} is flying."

    def sing(self):
        return f"{self.name} is singing."

class Penguin(Bird, Flyable):
    def fly(self):
        return f"{self.name} can't fly."

# High-level module that depends on abstractions (DIP)
def bird_info(bird):
    return f"{bird.name} says: {bird.sing()} and {bird.fly()}"

# Usage
sparrow = Sparrow("Sparrow")
penguin = Penguin("Penguin")

print(bird_info(sparrow))
print(bird_info(penguin))
