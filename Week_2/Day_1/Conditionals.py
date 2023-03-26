# Ask the user for a number between 1 and 100

# If the number is a multiple of three, print "Fizz"

# If the number is a multiple of five, print "Buzz".

# If the number is a multiple is a multiples of both three and five, print "FizzBuzz" instead.

user_number = int(input("Number Between 1 And 100"))
if user_number % 3 == 0 and user_number % 5 == 0:
    print("FizzBuzz")
elif user_number % 3 == 0:
    print("Fizz")
elif user_number % 5 == 0:
    print("Buzz")
