# Exercise 5: Longest word without a specific character
# Instructions

#     Keep asking the user to input the longest sentence they can without the character “A”.
#     Each time a user successfully sets a new longest sentence, print a congratulations message.
high_score = 0
while(1):
    sentence = input("Type the longest sentence WITHOUT an 'A', Good Luck! ")
    if 'a' in sentence:
        print("The senctence contains and 'A' try again!")
    else:
        if len(sentence) > high_score:
            print("Nice! New score!")
            high_score=len(sentence)
        else:
            print(f"Nice try, your high score is {high_score}")
