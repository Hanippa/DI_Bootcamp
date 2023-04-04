# Exercise 1 : Built-in functions
# Instructions

# Python has many built-in functions.
# If you feel that you don’t know how to properly implement them take a look at the python documentation online.

#     Write a program which prints the results of the following python built-in functions: abs(), int(), input().
#     Using the __doc__ dunder method create your own documentation which explains the execution of your code. Take a look at the doc method on google for help.


class Test:
    def __init__(self,num,str):
        self.num = num
        self.str = str
    def __str__(self):
        return str(self.num)
    def __abs__(self):
        return abs(self.num)
    def __input__(self):
        return input(self.str)
test = Test(-91 , "type : ")
print(abs(test))
print(input(test.str))

# 🌟 Exercise 2: Currencies
# Instructions

#     #Your code starts HERE


#     Using the code above, implement the relevant methods and dunder methods which will output the results below.
#     Hint : When adding 2 currencies which don’t share the same label you should raise an error.

# >>> c1 = Currency('dollar', 5)
# >>> c2 = Currency('dollar', 10)
# >>> c3 = Currency('shekel', 1)
# >>> c4 = Currency('shekel', 10)

# >>> str(c1)
# '5 dollars'

# >>> int(c1)
# 5

# >>> repr(c1)
# '5 dollars'

# >>> c1 + 5
# 10

# >>> c1 + c2
# 15

# >>> c1 
# 5 dollars

# >>> c1 += 5
# >>> c1
# 10 dollars

# >>> c1 += c2
# >>> c1
# 20 dollars

# >>> c1 + c3
# TypeError: Cannot add between Currency type <dollar> and <shekel>


class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount
    def __str__(self):
        return f"{self.amount} {self.currency}s"
    def __int__(self):
        return self.amount
    def __repr__(self):
        return f"{self.amount} {self.currency}s"
    def __add__(self,currency):
        if isinstance(currency, Currency):
            if self.currency == currency.currency:
                return self.amount + currency.amount
            else:
                return f"cannot add between {self.currency} and {currency.currency}"
        else:
            return self.amount + currency

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
print(str(c1))
print(int(c1))
print(repr(c1))
print(c1+c3)
c1 += c2
print(c1)