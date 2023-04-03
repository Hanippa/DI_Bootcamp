
try:
    user_pass = int(input("password: "))
    print("logged in")
except ValueError as passer:
    print("Not an integer" ,passer)
finally:
    print("brought to you by nestlle")
