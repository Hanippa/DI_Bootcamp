# Exercise 1


# Accept a number from the user and print its multiplication table

user_number = int(input("Enter A Number! : "))
for i in range(1, user_number+1):
    print("\n")
    for i2 in range(1, user_number+1):
        print(i*i2 , end=" ")

# Exercise 2


# Print the numbers from 1 to 10 using while loop
i=0
while  i < 10:
    i += 1
    print(i)