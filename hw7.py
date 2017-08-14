from sortedcontainers import SortedDict
"""
This code allows users to modify a dictionary of individuals, username pairs by adding and removing keys, value pairs. 
The user can also query the database for individuals by name or username
"""

# function print menu to user prior to prompting for input
def print_menu():
    print('1. Print Users')
    print('2. Add a User')
    print('3. Remove a User')
    print('4. Lookup user')
    print('5. Quit')
    print()

def get_name():
    bool = 0
    while bool < 1:
        input_str = input("Name: ")
        #check length of input
        if input_str.isalpha():
            bool = 1
        else:
            print("All characters in name must be alphabetic")
    return input_str

def get_username():
    bool = 0
    while bool < 1:
        input_str = input("User Name: ")
        #check length of username: length must be between 3 and 16 characters
        if len(input_str) > 2:
            if len(input_str) < 17:
                bool = 1
            else:
                print("Username cannot exceed 16 characters")
        else:
            print("Username must be at least 3 characters")
    return input_str

# Create dictionary with key = Names, value = user_name
usernames = SortedDict()
usernames['Summer'] = 'summerela'
usernames['William'] = 'GoofyFish'
usernames['Steven'] = 'LoLCat'
usernames['Zara'] = 'zanyZara'
usernames['Renato'] = 'songDude'

# setup counter to store menu choice
menu_choice = 0

# display your menu
print_menu()

# as long as the menu choice isn't "quit" get user options
while menu_choice != 5:
    # get menu choice from user
    menu_choice = int(input("Type in a number (1-5): "))

    # view current entries
    if menu_choice == 1:
        print("Current Users:")
        for x, y in usernames.items():
            print("Name: {} \tUser Name: {} \n".format(x, y))

    # add an entry
    elif menu_choice == 2:
        print("Add User")
        name = get_name()
        username = get_username()
        usernames[name] = username

    # remove an entry
    elif menu_choice == 3:
        print("Remove User")
        name = input("Name or Username: ")
        #compare key and value to user input to delete entry by individual or username
        for key, value in usernames.items():
            if name == key or name == value:
                print("Name: {}, User Name: {} has been removed\n".format(key, usernames[key]))
                del usernames[key]
                break

    # view user name
    elif menu_choice == 4:
        print("Lookup User")
        name = get_name()
        #check if name already exists in dictionary
        if name in usernames:
            print("{}'s username is: {}".format(name, usernames[name]))
        else:
            print("Username for {} was not found.".format(name))

    # is user enters something strange, show them the menu
    elif menu_choice != 5:
        print_menu()