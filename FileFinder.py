# import os
import glob  # glob is used for searching
# from pathlib import Path


def start_find():
    start = int(input("""What type of file do you want to find?\n
        1 - Document, 2 - Video, 3 - Audio, 4 - Photo\n> """))
    if start == 1:
        print("1\n\n\n")
        start_find()

    elif start == 2:
        print("2\n\n\n")
        start_find()

    elif start == 3:
        print("3\n\n\n")
        start_find()

    elif start == 4:
        print("4\n\n\n")
        start_find()

    else:
        print("Please provide a number.\n\n\n")
        start_find()


def file_find():
    file_search = input("What would you like to find:\n> ")
    file_type = input("What type of file are you looking for:\n> ")
    file_location = input("If you know the rough location let me know:\n> ")
    string = str(file_location + file_search + "." + file_type)
    result = glob.glob(f"{string}", recursive=True)
    print(result)


start_find()
