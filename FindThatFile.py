# import os
import glob  # glob is used for searching
# from pathlib import Path

type_file = "nul"


def start_find():
    global type_file
    start = int(input("""What type of file do you want to find?\n
        1 - Document, 2 - Video, 3 - Audio\n
        4 - Photo, 5 - Self-defined\n> """))
    if start == 1:
        print("1\n\n\n")
        type_file = "doc"

    elif start == 2:
        print("2\n\n\n")
        type_file = "vid"

    elif start == 3:
        print("3\n\n\n")
        type_file = "aud"

    elif start == 4:
        print("4\n\n\n")
        type_file = "imd"

    elif start == 5:
        print("5\n\n\n")
        type_file = "usr"

    else:
        print("Please provide a number.\n\n\n")
        start_find()


def file_find():
    file_search = input("What would you like to find?:\n> ")
    file_type = input("What type of file are you looking for?:\n> ")
    file_location = input("Where do you want to search?:\n> ")
    string = str(file_location + file_search + "." + file_type)
    result = glob.glob(f"{string}", recursive=True)
    print(result)




start_find()
