class Dog:
    def __init__(self, name,age,weight):
        self.name = name
        self.age = age
        self.weight = weight
    def bark(self):
        return f"{self.name} is barking"
    def run_speed(self):
        return (self.weight / self.age) *10
    def fight(self , other_dog):
        if self.run_speed() * self.weight > other_dog.run_speed() * other_dog.weight:
            return f"{self.name} won the fight"
        else:
            return f"{other_dog.name} won the fight"
# 🌟 Exercise 3 : Dogs Domesticated
# Instructions

#     Create a new python file and import your Dog class from the previous exercise.
#     In the new python file, create a class named PetDog that inherits from Dog.
#     Add an attribute called trained to the __init__ method, this attribute is a boolean and the value should be False by default.
#     Add the following methods:
#         train: prints the output of bark and switches the trained boolean to True

#         play: takes a parameter which value is a few names of other Dog instances (use *args). The method should print the following string: “dog_names all play together”.

#         do_a_trick: If the dog is trained the method should print one of the following sentences at random:
#             “dog_name does a barrel roll”.
#             “dog_name stands on his back legs”.
#             “dog_name shakes your hand”.
#             “dog_name plays dead”.
import random
class PetDog(Dog):
    def __init__(self, name, age, weight , trained=False):
        super().__init__(name, age, weight)
        self.trained = trained
    def train(self):
        self.trained = True
        print(self.bark())
    def play(self , *args):
        dogs_names = ''
        for i in args:
            dogs_names += i.name + ' '
        print(dogs_names ,'and' ,self.name , "All play together")
    def do_a_trick(self):
        if self.trained:
           print(random.choice([f"{self.name} does a barrel roll" , f"{self.name} stands on their back legs",f"{self.name} shakes your hand" , f"{self.name} plays dead"]))
        else:
            print(f"{self.name} is not trained")
