# PART 1

# In this exercise we will use PostgreSQL and Python. Create a new database and a new table in pgAdmin (or in psql). Read the instructions below before creating the new table

#     Create a new class called MenuItem, the attributes should be the name and price of each item.

#     Create several methods (save, delete, update) these methods will allow a user to save, delete and update items from the database.

#     Within the MenuItem class create a method called all which will return a list of all our MenuItem objects.

#     Create another method called get_by_name that will return a single MenuItem object depending on it’s name, if an object is not found (there is no item matching the name in the get_by_name method) return None.






import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = '2144'
DATABASE = 'resturant'


connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )

def run_select_query(query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
    return result
def run_change_query(query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        connection.commit()

class MenuItem:
    def __init__(self , name , price):
        self.name = name
        self.price = price
    def save(self):
        query = f'INSERT INTO menu (name , price) VALUES (\'{self.name}\' , money({self.price}))'
        run_change_query(query)
    def delete(self):
        query = f'DELETE FROM menu WHERE name = \'{self.name}\''
        run_change_query(query)
    def update(self , name , price):
        query = f'UPDATE menu SET price = money({price}) WHERE name = \'{name}\';'
        run_change_query(query)
    @classmethod
    def get_by_name(cls , name):
        query = f'SELECT * FROM menu WHERE name = \'{name}\';'
        return run_select_query(query)
    @classmethod
    def all(cls):
        query = 'SELECT * FROM menu;'
        return run_select_query(query)


# item = MenuItem('Salad', 12)
# item.save()
# item.delete()
# item.update('Burger', 37)
# item2 = MenuItem.get_by_name('Salad')
# print(item2)
# query = 'SELECT * FROM menu;'
# print(run_select_query(query))
# items = MenuItem.all()
# print(items)


# Part 2

#     Create a file called menu_editor.py
