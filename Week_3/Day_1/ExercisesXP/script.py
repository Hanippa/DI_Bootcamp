# 🌟 Exercise 1: Cats
# Instructions

# Using this class

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

#     Instantiate three Cat objects using the code provided above.
#     Outside of the class, create a function that finds the oldest cat and returns the cat.
#     Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.


cats = [Cat("tracy", "6") , Cat("gary", "2") ,  Cat("missy", "3")]

def oldest(cats):
    oldest = Cat("",0)
    for i in cats:
        if int(i.age) > int(oldest.age):
            oldest = i
    return oldest.name
print("Exercise 1 : ",oldest(cats))

# 🌟 Exercise 2 : Dogs
# Instructions

#     Create a class called Dog.
#     In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.
#     Create a method called bark that prints the following string “<dog_name> goes woof!”.
#     Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
#     Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
#     Print the details of his dog (ie. name and height) and call the methods bark and jump.
#     Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
#     Print the details of her dog (ie. name and height) and call the methods bark and jump.
#     Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.

class Dog:
    def __init__(self, name , height):
        self.height = height
        self.name = name
    def bark(self):
        print(f"{self.name} goes woof!")
    def jump(self):
        self.x = self.height*2
        print(f"{self.name} jumps {self.x} cm high!")
dogo = Dog("lassy", 11)
print("Exercise 2 : ")
dogo.bark()
dogo.jump()
davids_dog = Dog("Rex", 50)
print(davids_dog.name ,"  ", davids_dog.height)
davids_dog.bark()
davids_dog.jump()
sarahs_dog = Dog("Teacup", 20)
print(sarahs_dog.name ,"  ", sarahs_dog.height)
sarahs_dog.bark()
sarahs_dog.jump()

print(davids_dog.name if davids_dog.height > sarahs_dog.height else sarahs_dog.name)


# 🌟 Exercise 3 : Who’s the song producer?
# Instructions

#     Define a class called Song, it will show the lyrics of a song.
#     Its __init__() method should have two arguments: self and lyrics (a list).
#     Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.

#     Create an object, for example:

#     stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])


#     Then, call the sing_me_a_song method. The output should be:

#     There’s a lady who's sure
#     all that glitters is gold
#     and she’s buying a stairway to heaven

class Song:
    def __init__(self, lyrics:list):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        print('\n'.join([x for x in self.lyrics]))

stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])

stairway.sing_me_a_song()


# Exercise 4 : Afternoon at the Zoo
# Instructions

#     Create a class called Zoo.
#     In this class create a method __init__ that takes one parameter: zoo_name.
#     It instantiates two attributes: animals (an empty list) and name (name of the zoo).
#     Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.
#     Create a method called get_animals that prints all the animals of the zoo.
#     Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list.

#     Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
#     Example

#     { 
#         1: "Ape",
#         2: ["Baboon", "Bear"],
#         3: ['Cat', 'Cougar'],
#         4: ['Eel', 'Emu']
#     }


#     Create a method called get_groups that prints the animal/animals inside each group.
#     Create an object called ramat_gan_safari and call all the methods.
#     Tip: The zookeeper is the one who will use this class.
#     Example

#     Which animal should we add to the zoo --> Giraffe
#     x.add_animal(Giraffe)

class Zoo:
    def __init__(self,zoo_name):
        self.name = zoo_name
        self.animals = []
    def add_animal(self,new_animal):
        self.animals.append(new_animal) if not self.animals.count(new_animal) else print(new_animal,"Already in list")
    def get_animals(self):
        print(*self.animals)
    def sell_animal(self, animal_sold):
       self.animals.remove(animal_sold) if self.animals.count(animal_sold)>0 else print(animal_sold,"Not in list")
    def sort_animals(self):
        animal_dict ={}
        self.animals.sort()
        print(self.animals)
        for i in range(len(self.animals)-1):
            if self.animals[i][0] == self.animals[i+1][0]:
               animal_dict[len(animal_dict)+1] = [self.animals[i]]
               animal_dict[len(animal_dict)].append(self.animals[i+1])
                

        print(animal_dict)
            

fzoos = Zoo("Fzoos")
fzoos.add_animal("Emo")
fzoos.add_animal("Giraffe")
fzoos.add_animal("Cat")
fzoos.add_animal("Cougar")
fzoos.add_animal("Eel")
fzoos.add_animal("Bear")
fzoos.add_animal("Baboon")

fzoos.add_animal("Baboon")
fzoos.sell_animal("Bee")
fzoos.get_animals()
fzoos.sort_animals()