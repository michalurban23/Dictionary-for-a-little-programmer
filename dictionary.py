import csv
import os
import sys


# Main menu of the program
def menu():
    os.system("clear")
    print("Dictionary for a little programmer\n")
    print("1) Search for a definition by its name")
    print("2) Add a new definition")
    print("3) Show a full list of definitions")
    print("4) Show definitions by its first letter")
    print("0) Exit")
    option = choice()


# Foolproof input choice:
def choice():
    while True:
        option = input("")
        if option not in ["0", "1", "2", "3", "4"]:
            print("Pick a number 1 - 4, or 0 to exit ")
            continue
        else:
            return option


# Return to main menu:
def return_menu():
    menu()


# Search the content for a definition:
def search():
    fgfgf


# Adds a definition to the content:
def add():
    fgfgf


# Shows all possible definitions:
def show_all():
    fgfgf


# Ask for a first letter then show possibilities:
def show_available():
    fgfgf


# Open a file and save to a dictionary:
dictionary = {}
with open('dictionary.csv', newline='\n') as csvfile:
    content = csv.reader(csvfile, delimiter=',')
    for line in content:
        dictionary[line[0]] = line[1], line[2]

while True:
    choice = menu()
    if choice == "1":
        search()
    elif choice == "2":
        add()
    elif choice == "3":
        show_all()
    elif choice == "4":
        show_available()
    else:
        break
