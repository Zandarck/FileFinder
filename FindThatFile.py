# import os
import glob  # glob is used for searching
# from pathlib import Path

file_type = "nul"
file_name = "nul"
file_location = "nul"


def start_find():
    global file_type
    start = int(input("""What type of file do you want to find?\n
        1 - Document, 2 - Video, 3 - Audio\n
        4 - Photo, 5 - Self-defined\n> """))
    if start == 1:
        print("1\n\n\n")
        file_type = "doc"
        choice_find()

    elif start == 2:
        print("2\n\n\n")
        file_type = "vid"
        choice_find()

    elif start == 3:
        print("3\n\n\n")
        file_type = "aud"
        choice_find()

    elif start == 4:
        print("4\n\n\n")
        file_type = "img"
        choice_find()

    elif start == 5:
        print("5\n\n\n")
        file_type = "usr"
        choice_find()

    else:
        print("Please provide a number.\n\n\n")
        start_find()


def choice_find():
    global file_name
    global file_type
    global file_location
    if file_type == "doc":
        print("Searching for documents")
        file_name = input("What would you like to find?:\n> ")
        file_location = input("Where do you want to search?:\n> ")
        user_file_find(file_name, file_type, file_location)

    elif file_type == "vid":
        print("Searching for videos")
        file_name = input("What would you like to find?:\n> ")
        file_location = input("Where do you want to search?:\n> ")
        user_file_find(file_name, file_type, file_location)

    elif file_type == "aud":
        print("Searching for audio tracks")
        file_name = input("What would you like to find?:\n> ")
        file_location = input("Where do you want to search?:\n> ")
        user_file_find(file_name, file_type, file_location)

    elif file_type == "img":
        print("Searching for images")
        file_name = input("What would you like to find?:\n> ")
        file_location = input("Where do you want to search?:\n> ")
        user_file_find(file_name, file_type, file_location)

    elif file_type == "usr":
        print("Searching for user defined extention")
        file_name = input("What would you like to find?:\n> ")
        file_type = input("What type of file are you looking for?:\n> ")
        file_location = input("Where do you want to search?:\n> ")
        user_file_find(file_name, file_type, file_location)


def user_file_find(name, type, local):
    string = str(file_location + file_name + "." + file_type)
    result = glob.glob(f"{string}", recursive=True)
    print(result)
    print(string)


start_find()
