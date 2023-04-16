
#     You will have to create two classes:
#         Human
#         Queue


# Human

# Represents a citizen of the city, it has the following attributes: id_number (str), name (str), age (int), priority (bool) and blood_type (str). Its blood type can be “A”, “B”, “AB” or “O”.

# This class has no methods.


# Queue

# Represents a queue of humans waiting for their vaccine.
# It has the following attribute : humans, the list containing the humans that are waiting. It is initialized empty.

# This class is useful to manage who will get vaccinated in priority. It has the following methods:

#     add_person(self, person) : Adds a human to the queue, if he is older than 60 years old or a priority person, put him at the beginning of the list (at index 0) before every other.

#     find_in_queue(self, person) : Returns the index of a human in the queue.

#     swap(self, person1, person2): Swaps person1 with person2.

#     get_next(self) : Returns the next human waiting in the queue. The next human should be the one located at the index 0 in the list.

#     get_next_blood_type(self, blood_type) : Returns the first human with this specific blood type.

#     sort_by_age(self) : Sorts the queue
#         first the priority people
#         then, the older people
#         then the younger people

# Every human returned by get_next and get_next_blood_type is removed from the list.
# Those functions return None if the list is empty (ie. no one in the list). 

class Human:
    def __init__(self, id_number , name , age , priority,blood_type):
        self.id_number = id_number
        self.name = name
        self.age = age
        self.priority = priority
        self.blood_type = blood_type
        self.family = []
    def __repr__(self):
        return self.age
    def __gt__(self , item):
        return self.age > item.age
    def add_family_member(self, person):
        self.family.append(person)
        person.family.append(self)
class Queue:
    def __init__(self):
        self.humans = []
    def add_person(self, person):
        if person.age > 60 or person.priority:
            self.humans.insert(0, person)
        else:
            self.humans.append(person)
    def find_in_queue(self, person):
        return self.humans.index(person)
    def swap(self, person1, person2):
        person1_index = self.find_in_queue(person1)
        person2_index = self.find_in_queue(person2)
        self.humans.insert(person1_index, person2)
        self.humans.insert(person2_index, person1)
    def get_next(self):
        temp = self.humans[0]
        del self.humans[0]
        return temp.name
    def get_next_blood_type(self,blood_type):
        for count , i in enumerate(self.humans):
            if i.blood_type == blood_type:
                temp = self.humans[count]
                del self.humans[count]
                return temp.name
        return False
    def sort_by_age(self):
        self.humans = list(reversed(sorted(self.humans)))
        for i in range(len(self.humans)):
            if self.humans[i].priority:
                self.humans.insert(0 , self.humans[i])
                self.humans.remove(self.humans[i])
    def rearange_queue(self):
        for i in range(len(self.humans)):
            if self.humans[i].name in self.humans[i+1].family:
                self.swap( self.humans[i+1].family,  self.humans[i+2].family)


humy = []
humy.append(Human("90834534", "Marinet",30, True, 'B'))
humy.append(Human("15235234", "IceSpice", 21, False, 'AB'))
humy.append(Human("63453450", "Nicky", 28, False, 'A'))
humy.append(Human("15435544", "Cardy", 29, False, 'O'))
humy.append(Human("15435235", "Boga", 31, False, 'B'))
humy.append(Human("34234324", "Billy", 67, False, 'A'))
humy.append(Human("90972340", "Sneed", 99, False, 'AB'))
humy.append(Human("98572893", "Kenny", 30, False, 'O'))
humy.append(Human("89234342", "Casy", 15, True, 'AB'))
humy.append(Human("98293423", "Erold", 51, False, 'A'))
humy.append(Human("23423523", "Stacy", 25, False, 'AB'))

clalit = Queue()
for i in humy:
    clalit.add_person(i)
print([x.name +" - "+ str(x.age) for x in clalit.humans])
clalit.sort_by_age()
print([x.name +" - "+ str(x.age) for x in clalit.humans])
print(clalit.get_next())
print(clalit.get_next())
print(clalit.get_next())
print([x.name +" - "+ str(x.age) for x in clalit.humans])



# Part 2  
# Human

# Create an attribute family for the Human class.

# Initialized as empty, family is a list of all the humans that are living in the same house with this human.
# Add a method add_family_member(self, person) that adds the person to this human’s family and this human to the person’s family.


# Queue

# Add the rearange_queue(self) method to the Queue class, so that there won’t be two members of the same family one after the other in the line.