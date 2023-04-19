# Part 2

#     Create a file called menu_editor.py , which will have the following functions:
#         load_manager()- this function should create a new MenuItem instance.

#         show_user_menu() - this function should display the program menu (not the restaurant menu!),
#            and ask the user to choose an item. Call the appropriate function that matches the user’s input. 
import menuitem

def load_manager(name , price):
    return menuitem.MenuItem(name, price)
def show_user_menu(item):
    print(f"WELCOME TO THE MENU MANAGEMENT SYSTEM WHAT WOULD LIKE to DO? : \n(a) ADD AN ITEM TO THE MENU\n(u) UPDATE AN ITEM ON THE MENU\n(d) DELETE AN ITEM ON THE MENU\n(v) VIEW THE MENU\n(g) GET AN ITEM BY NAME\n(x) EXIT")
    user_in = input(" : ")
    if user_in in ['a' , 'u' , 'd' , 'v' , 'g' , 'x']:
        while user_in != 'x':
            if user_in == 'a':
                add_item_to_menu(item)
            elif user_in == 'u':
                update_menu_item()
            elif user_in == 'd':
                remove_item_from_menu(item)
            elif user_in == 'v':
                print(show_restaurant_menu())
            elif user_in == 'g':
                get_item_by_name(item)
            print(f"WELCOME TO THE MENU MANAGEMENT SYSTEM WHAT WOULD LIKE to DO? : \n(a) ADD AN ITEM TO THE MENU\n(u) UPDATE AN ITEM ON THE MENU\n(d) DELETE AN ITEM ON THE MENU\n(v) VIEW THE MENU\n(g) GET AN ITEM BY NAME\n(x) EXIT")
            user_in = input(" : ")
        print(show_restaurant_menu())
        return
    else:
        print(f'OPTION {user_in} NOT VALID')

def add_item_to_menu(item):
    item.name = input('NAME : ')
    item.price = input('PRICE : ')
    item.save()
def remove_item_from_menu(item):
    if item.name:
        item.delete()
def show_restaurant_menu():
    return menuitem.MenuItem.all()
def update_menu_item(item):
    name = input('ITEM NAME : ')
    price = input('NEW PRICE : ')
    item.update(name , price)
def get_item_by_name(item):
    name = input('ITEM NAME : ')
    item.get_by_name(name)

item = load_manager('', 0)
show_user_menu(item)