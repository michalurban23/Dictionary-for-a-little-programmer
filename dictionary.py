import csv
import os
import sys


def menu():
    os.system("clear")
    print("Dictionary for a little programmer\n")
    print("1) Search for a definition by its name")
    print("2) Add a new definition")
    print("3) Show a full list of definitions")
    print("4) Show definitions by its first letter")
    print("0) Exit")
    option = choice()


def choice():
    while True:
        option = input("")
        if option not in ["0", "1", "2", "3", "4"]:
            print("Pick a number 1 - 4, or 0 to exit ")
            continue
        else:
            return option


def return_menu():
    menu()


def search():
    fgfgf


def add():
    fgfgf


def show_all():
    fgfgf


def show_available():
    fgfgf


def exit_prog():
    fgfgf


# Open a file and save to a dictionary:
dictionary = {}
with open('dictionary.csv', newline='\n') as csvfile:
    content = csv.reader(csvfile, delimiter=',')
    for line in content:
        dictionary[line[0]] = line[1], line[2]


os.system("clear")
print(*dictionary["multithreading"])
choice = menu()
if choice == "0":
    sys.exit()
