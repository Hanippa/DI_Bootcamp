# What you will create

# Use python to create a Hangman game.


# Instructions

#     The computer choose a random word and mark stars for each letter of each word.
#     Then the player will guess a letter.
#         If that letter is in the word(s) then the computer fills the letter in all the correct positions of the word.
#         If the letter isn’t in the word(s) then add a body part to the gallows (head, body, left arm, right arm, left leg, right leg).
#         The player will continue guessing letters until they can either solve the word(s) (or phrase) or all six body parts are on the gallows.
#         The player can’t guess the same letter twice.







import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist) 

    ### YOUR CODE STARTS FROM HERE ###
Hang = [ '''
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||
| |/         ||
| |          ||
| |          
| |        
| |       
| |       
| |     
| |    
| |          
| |          
| |          
| |          
| |        
            
'''
,
'''
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |       
| |      
| |   
| |    
| |          
| |         
| |          
| |         
| |         
            
'''
,
'''
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |         Y . . Y
| |          |   | 
| |          | . | 
| |          |   |
| |         
| |         
| |         
| |         
| |         
          
'''
,
'''
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |        /Y . . Y
| |      .// |   | 
| |      //  | . | 
| |     ')   |   |   
| |          
| |         
| |         
| |          
| |        
           
'''
,
'''
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |        /Y . . Y\\
| |      .// |   | \\\\
| |      //  | . |  \\\\
| |     ')   |   |   (`
| |          
| |          
| |         
| |          
| |         
            
'''
,
'''
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |        /Y . . Y\\
| |      .// |   | \\\\
| |      //  | . |  \\\\
| |     ')   |   |   (`
| |          ||'
| |          || 
| |          || 
| |          || 
| |         / | 
            `-' 
'''
,
'''
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |        /Y . . Y\\
| |      .// |   | \\\\
| |      //  | . |  \\\\
| |     ')   |   |   (`
| |          ||'||
| |          || ||
| |          || ||
| |          || ||
| |         / | | \\
            `-' `-'
'''
]
og_word = word
user_guess = list('*'*len(word))
count = 0
print("\n", "\n" ,f"Welcome to HangMan! A word guessing game! start by guessing a letter in the word, but be careful if you get it wrong too many times you might not make it to see the word")
print(Hang[0])
while ''.join(user_guess) != og_word:
    print("Guess A letter ! ", *user_guess)
    user_letter = input("Letter : ")
    if word.find(user_letter) != -1:
        for i in range(word.count(user_letter)):
            user_guess[word.find(user_letter)] = word[word.find(user_letter)]
            word = word[:word.find(user_letter)] + "-" + word[word.find(user_letter)+1:]
    else:
        count += 1
        print(Hang[count])
    if count > 5:
        print("You Lose :( ","\n","\n")
        break
if ''.join(user_guess) == og_word:
    print("You win! The word is : ", og_word)