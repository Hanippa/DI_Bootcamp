# Exercise 1 : Authentication database


# Instructions
# PART 1: Authentication CLI - login:

#     Create a dictionary that contains users: each key will represent a username, and each value will represent that user’s password. Initialize this dictionary with 3 users & passwords.
#     Create a loop that does the following:
#         If the user inputs “exit”, break out of the loop.
#         If the user inputs “login”, ask them for their username and password.
#             If the user’s details exist print “you are now logged in”.
#             If the user is successfully logged in, store the username in a variable called logged_in so we can track it later.

# PART 2 : Authentication CLI - signup:

# Continuation of the Exercise Above - Authentication CLI - login

#     If the user does not exist ask if they would like to sign up:
#         Ask the user for a username and make sure it doesn’t exist as a key in our dictionary, if the username is not valid continue asking the user to input a username.
#         Ask the user for a password. The password is the value.
import psycopg2
from hashlib import sha256

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = '2144'
DATABASE = 'Users'


connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )

def insert_new_user(user_name , password):
    with connection.cursor() as cursor:
        cursor.execute(f"INSERT INTO users (user_name , password) VALUES ('{user_name}' , '{password}');")
        connection.commit()
def get_dict():
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM users;')
        result = cursor.fetchall()
    return dict(result)

logged_in = ''

users = get_dict()
user_in = input("login / exit : ")
while user_in != 'exit':
    if user_in == 'login':
        user_name = input("What is your user name? : ")
        if user_name in users.keys():
            user_password = input("What is your password? : ")
            print(hash(user_password) , users[user_name])
            if users[user_name] == sha256(user_password):
                print("Logged In")
                logged_in = user_name
                break
        su_choice = input("User Does Not Exist Would You Like To Sign Up ? (y/n) : ")
        if su_choice == 'y':
                user_password = input("What is your password? : ")
                users[user_name] = user_password
                insert_new_user(user_name, sha256(user_password))
                print("Account regisetered successfully!")
                    

    user_in = input("login / exit : ")
