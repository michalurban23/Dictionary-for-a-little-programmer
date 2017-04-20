import csv
import os
import sys
import os.path


# Main menu of the program
def menu():
    os.system("clear")
    print("Dictionary for a little programmer\n")
    print("1) Search for a definition by its name")
    print("2) Add a new definition")
    print("3) Show a full list of definitions")
    print("4) Show definitions by its first letter")
    print("0) Exit")
    pick = input_choice()
    return pick


# Foolproof input choice:
def input_choice():
    while True:
        option = input("\nSelect an option: ")
        if option not in ["0", "1", "2", "3", "4"]:
            print("Pick a number 1 - 4, or 0 to exit ")
            continue
        else:
            return option


# Return to main menu:
def return_menu():
    while True:
        rtrn = input("\nPress enter to go back to main menu ")
        if rtrn == "":
            break


# Search the content for a definition:
def search_def(dictionary):
    os.system("clear")
    while True:
        user_search = input("What are you looking for? (type 0 to return)\n")
        if user_search in dictionary:
            os.system("clear")
            print(user_search.title(), "-", dictionary[user_search][0])
            print("Source -", dictionary[user_search][1])
            break
        elif user_search == "0":
            break
        else:
            print("\nThis definition is not in the dictionary yet. Try different one.\n")
    return_menu()


# Adds a definition to the content (and refresh dictionary afterwards):
def add_def():
    while True:
        os.system("clear")
        new_name = input("Please enter name of your new definition (or 0 to exit): \n")
        if new_name == "0":
            break
        new_def = input("Please enter the definition: \n")
        new_source = input("Please enter the source (or your credentials): \n")
        entr = input("Thanks for this entry. Press enter to continue")
        with open('dictionary.csv', 'a', newline='\n') as csvfile:
            content = csv.writer(csvfile, delimiter=',')
            content.writerow([new_name, new_def, new_source])
    load_dict()
    return_menu()


# Shows all possible definitions:
def show_all(dictionary):
    os.system("clear")
    print("Available definitions: \n")
    for item in range(len(dictionary)):
        print(sorted(dictionary)[item])
    return_menu()


# Ask for a first letter then show possibilities:
def show_available(dictionary):
    os.system("clear")
    while True:
        zero_match = 0
        first_letter = input("Enter first letter (or 0 to return): ")
        if first_letter == "0":
            break
        if not (first_letter.isalpha() and len(first_letter) == 1):
            continue
        print("\nAvailable definitions: \n")
        for item in range(len(dictionary)):
            if sorted(dictionary)[item][0] == first_letter.lower():
                print(sorted(dictionary)[item])
            else:
                zero_match += 1
        print("")
        if zero_match == len(dictionary):
            print("Couldn't find any matching definitions. Try a different letter.\n")
    return_menu()


# Open a file and save to a dictionary:
def load_dict():
    dictionary = {}
    with open('dictionary.csv', newline='\n') as csvfile:
        content = csv.reader(csvfile, delimiter=',')
        for line in content:
            dictionary[line[0]] = line[1], line[2]
    return dictionary


# Check if the CSV file exists:
if not os.path.isfile("dictionary.csv"):
    print("\nThere is no dictionary.csv file in program directory. Please download it from the repository.\n")
    sys.exit()

# Main program:
updated_dict = load_dict()
while True:
    user_choice = menu()
    if user_choice == "1":
        search_def(updated_dict)
    elif user_choice == "2":
        add_def()
        updated_dict = load_dict()
    elif user_choice == "3":
        show_all(updated_dict)
    elif user_choice == "4":
        show_available(updated_dict)
    else:
        sys.exit()
