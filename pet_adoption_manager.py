
from datetime import datetime

class Adopter:
    adoption_contract = []
    adoption_list = []
    def __init__(self, name, contact, address, shelter=None):
        self.adopted_date = None
        self.contact = contact
        self.address = address
        self.name = name
        self.shelter = shelter
        
    def __str__(self):
        return f"name: { self.name}, shelter: {self.shelter}, contact : {self.contact}, address : {self.address}"
        
    def adopt_animal(self, list_of_animals):
        shelter = self.shelter.list_animals_
        if (shelter) :
            for animal in shelter:
                if not animal.name in list_of_animals:
                    continue
                animal.adopted = True
                self.adopted_date = datetime.now()
                self.shelter.list_animals_ = shelter
                Adopter.adoption_contract.append(self) 
                Adopter.adoption_list.append(animal)
    
    @classmethod
    def list_adopted_animals(cls):
        return [str(animal) for animal in cls.adoption_list]
    
    @classmethod
    def adoption_contract_list(cls):
        return [str(adopted_list) for adopted_list in cls.adoption_contract]


class Animal:
    all_animals = []
    
    
    def __init__(self, name,species, age=None):
        self.name = name
        self.species = species
        self.age = age
        self.adopted = False
        
        Animal.all_animals.append(self)
        
    def __str__(self):
        return f"name:{ self.name}, species: {self.species}, adopted : {self.adopted}"
        
    def estimate_age(self,beak=None , beak_color=None, teeth=None , teeth_color=None) :
        if self.species == "Mammal" and teeth:
            self.age = 3 if teeth_color == 'white' else 8
        elif self.species == "Bird" and beak: 
            self.age = 3 if  beak_color == "bright" else 8
        
    
# Cat, Dog, Parrot, CityBird inherit from Animal.
class Cat(Animal):
    pass
class Dog(Animal):
    pass
class Parrot(Animal):
    pass

class CityBird(Animal):
    pass




class Shelter:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.adopted_animals_counter = 0
        self.total_animals_in_shelter = 0
        self.list_animals_ = []
                
    def add_animal(self, animal):
        animal.adopted = False
        if animal  not in self.list_animals_:
            self.list_animals_.append(animal)
        
        return self.list_animals_

    def number_of_adopted_animals(self) :
        for animal in self.list_animals_:
            if not animal.adopted:
                continue
            self.adopted_animals_counter += 1
        return self.adopted_animals_counter

    def list_animals(self):
        return [ str(animal)   for animal in self.list_animals_]
        
shelter = Shelter("Happy Tails", "Nairobi")
shelter.add_animal(Cat("Milo", "Mammal", 3))
shelter.add_animal(Dog("Bruno", "Mammal", 3))
person_adopting = Adopter("Mary", "mary@gmail.com", "Bookio",shelter)
# shelter.adopt_animal("Bruno")
person_adopting.adopt_animal(["Bruno", "Milo"])
print(
{'contract' : person_adopting.adoption_contract_list()} , 
{'list of adopted animals' :person_adopting.list_adopted_animals()}
)
print(shelter.number_of_adopted_animals())
# animal = Dog("Milo", "Mammal")
# animal.estimate_age(False, None, True, "white")
# print(animal.age)
# print(shelter.list_animals())
