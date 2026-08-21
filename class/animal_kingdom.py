"""
Create an abstract class Animal with  methods is_marine(),
is_vertebrate(), can_fly(), is_warmblooded()

Create classes Fish, Bird, Mammal, Reptile that inherit Animal. 

Create another child class Human that inherits Mammal. 
In case of human
- Add human's name and country in the constructor
- Also add get_name() and get_country()

Also add appropriate unit test to test your code. 

"""

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def is_marine():
        pass

    @abstractmethod
    def is_vertebrates():
        pass

    @abstractmethod
    def can_fly():
        pass

    @abstractmethod
    def is_warmblooded():
        pass


class Fish(Animal):
    def __init__(self, name):
        self.name = name
     
    def is_marine(self):
        return True

    def is_vertebrates(self):
        return True
    
    def can_fly(self):
        return False
    
    def is_warmblooded(self):
        return False

    def get_name(self):
        return self.name


myanimal = Fish("salmon")
assert myanimal.is_warmblooded() == False
assert myanimal.is_marine() == True
assert myanimal.can_fly() == False
assert myanimal.is_vertebrates() == True
assert myanimal.get_name() == "salmon"

class Bird(Animal):
    def __init__(self, name):
        self.name = name

    def is_marine(self):
        return False
    
    def is_vertebrates(self):
        return True
    
    def can_fly(self):
        return True
    
    def is_warmblooded(self):
        return True

    def get_name(self):
        return self.name
    
myanimal = Bird("squirel")
assert myanimal.is_warmblooded() == True
assert myanimal.is_marine() == False
assert myanimal.can_fly() == True
assert myanimal.is_vertebrates() == True
assert myanimal.get_name() == "squirel"

class Mammal(Animal):
    def __init__(self, name):
        self.name = name

    def is_marine(self):
        return True

    def is_vertebrates(self):
        return True

    def can_fly(self):
        return False

    def is_warmblooded(self):
        return True

    def get_name(self):
        return self.name
    
myanimal = Mammal("dog")
assert myanimal.is_warmblooded() == True
assert myanimal.is_marine() == True
assert myanimal.is_vertebrates() == True
assert myanimal.can_fly() == False
assert myanimal.get_name() == "dog"

class Reptiles(Animal):
    def __init__(self, name):
        self.name = name

    def is_marine(self):
        return True
    
    def is_vertebrates(self):
        return False
    
    def can_fly(self):
        return False
    
    def is_warmblooded(self):
        return False

    def get_name(self):
        return self.name

myanimal = Reptiles("snakes")
assert myanimal.can_fly() == False
assert myanimal.is_marine() == True
assert myanimal.is_vertebrates() == False
assert myanimal.is_warmblooded() == False
assert myanimal.get_name() == "snakes"

class Human(Mammal):
    def __init__(self, name, address):
        self.name = name
        self.address = address
     
    def is_marine(self):
        return False

    def is_vertebrates(self):
        return True
    
    def can_fly(self):
        return False
    
    def is_warmblooded(self):
        return True

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address
    
    
wehuman = Human("puja", "jyamire")
assert wehuman.is_marine() == False
assert wehuman.can_fly() == False
assert wehuman.is_warmblooded() == True
assert wehuman.get_name() == "puja"
assert wehuman.get_address() == "jyamire"
assert wehuman.is_vertebrates() == True



    

    

   



