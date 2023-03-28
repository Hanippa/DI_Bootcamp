# Exercise 1 
alpha = 'אבגדה'

heb_dict = dict(enumerate(alpha))
even = heb_dict[value for key, value in heb_dict.items() if value % 2 == 0]
print(even)