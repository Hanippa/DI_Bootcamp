# Instructions
# Part 1 : Quizz :

# Answer the following questions

#     What is a class?               A class in an object wrapper, and all object under the class will inherit from it.
#     What is an instance?           A sigular object constructed by the __init__(constructor) in the class.
#     What is encapsulation?         The concept of encapsulating object date in another method.
#     What is abstraction?           The idea of making abstract charatersitics of an object and then creating more class to be more specific.
#     What is inheritance?           Taking methods/variables/charateristics from the paret object.
#     What is multiple inheritance?  The same as regualr inheritence but when you take from mutiple object.
#     What is polymorphism?          The ability to inherit, and change the form of the inherited charaterisitcs
#     What is method resolution order or MRO? Its the order in which an object inherits from its parents.





# Part 2: Create a deck of cards class.

# The Deck of cards class should NOT inherit from a Card class.

# The requirements are as follows:

#     The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
#     The Deck class :
#         should have a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
#         should have a method called deal which deals a single card from the deck. After a card is dealt, it should be removed from the deck.
import random
class Card:
    def __init__(self , suit , value):
        self.suit = suit
        self.value = value

class Deck:
    def __init__(self , deck):
        self.deck = deck
    def shuffle(self):
        if len(self.deck) > 51:
            self.deck.shuffle()
    def dead(self , num):
        print(self.deck[num].suit , self.deck[num].value)
        del self.deck[num]
        
decko = []
for i in range(52):
    i = Card(random.choice(["Hearts" , "Diamonds" , "Clubs" , "Spades"]), random.randint(0, 10))
    decko.append(i)
blast = Deck(decko)
blast.shuffle
print(blast.deck[0].suit)