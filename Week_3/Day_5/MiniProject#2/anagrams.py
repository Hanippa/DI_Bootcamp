    # Now create another Python file, called anagrams.py. This will contain all the UI (user interface) functionality of your program, and will rely on AnagramChecker for the anagram-related logic.

    # It should do the following:
    #     Show a menu, offering the user to input a word or exit. Keep showing the menu until the user chooses to exit.

    #     If the user chooses to input a word, it must be accepted from the user’s keyboard input, and then be validated:
    #         Only a single word is allowed. If the user typed more than one word, show an error message. (Hint: how do we know how many words were typed?)
    #         Only alphabetic characters are allowed. No numbers or special characters.
    #         Whitespace should be removed from the start and end of the user’s input.

    #     Once your code has decided that the user’s input is valid, it should find out the following:
    #         All possible anagrams to the user’s word.
    #         Create an AnagramChecker instance and apply it to the steps created above.
    #         Display the information about the word in a user-friendly, nicely-formatted message such as:


    #         YOUR WORD :”MEAT”
    #         this is a valid English word.
    #         Anagrams for your word: mate, tame, team.
from anagram_checker import AnagramChecker
def get_user_menu_choice():
    print(f"\nWELCOME TO ANAGRAY!\nMEMU:\n(i) - INPUT A WORD\n(q) - QUIT\n")
    user_in = input("-> : ")
    if user_in in ["i" , "q"]:
        return user_in
    else:
        raise ValueError("CHOICE NOT VALID")

def get_user_ana():
    ana = AnagramChecker()
    user_in = ''.join(filter(str.isalpha,  input("INPUT YOUR WORD : ")))
    while not ana.is_valid_word(user_in):
        user_in = ''.join(filter(str.isalpha,  input("INPUT YOUR WORD : ")))
    return user_in


ana = AnagramChecker()


if get_user_menu_choice() == "i":
    print(f"This is a Valid english word\nAnagrams for your word: {' , '.join(ana.get_anagrams(get_user_ana())).lower()}")
else:
    print("BYE!")

