# Part II - rock-paper-scissors.py

#     rock-paper-scissors.py : create 3 functions
#         get_user_menu_choice() - this should display a simple menu, get the user’s choice (with data validation), and return the choice. No looping should occur here.
#         The possibles choices are : Play a new game or Show scores or Quit

#         print_results(results) – this should print the results of the games played. It should have a single parameter named results; which will be a dictionary of the results of the games played. It should display these results in a user-friendly way, and thank the user for playing.


#         Note: results should be in this form: {win: 2,loss: 4,draw: 3}. Bear in mind that this dictionary will need to be created and populated in some other part of our code, and passed in to the print_results function at the right time.

#         main() - the main function. It should take care of 3 things:
#             Displaying the menu repeatedly, until the user types in the value to exit the program: ‘x’ or ‘q’, whatever you decide. (Make use of the get_user_menu_choice function)

#             When the user chooses to play a game:
#                 Create a new Game object (see below), and call its play() function, receiving the result of the game that is returned.
#                 Remember the results of every game that is played.

#             When the user chooses to exit the program, call the print_results function in order to display a summary of all the games played.
from game import Game
import re
def get_user_menu_choice():
    print(f"\nWELCOME TO Xrps!\nMEMU:\n(p) - PLAY\n(s) - SHOW SCORES\n(q) - QUIT\n")
    user_in = input("-> : ")
    if user_in in ["q" , "s" , "p"]:
        return user_in
    else:
        raise ValueError("CHOICE NOT VALID")
def print_results(results):
    print(f"GAME RESULTS\n-> YOU HAVE WON {results['win']} GAMES\n-> YOU HAVE LOST {results['loss']} GAMES\n-> YOU HAVE DREW {results['draw']} GAMES")
def main():
    menu_in = get_user_menu_choice()
    results = {"win" : 0 , "loss" : 0 , "draw" : 0}
    while menu_in != "q":
        if menu_in == "s":
            print_results(results)
        else:
            game = Game({"rock" : "scissors" , "paper" : "rock" , "scissors" : "paper"})
            results[game.play()] += 1
        menu_in = get_user_menu_choice()
    print_results(results)
    return
main()