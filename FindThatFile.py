import glob  # glob is used for searching


def start_find():
    start = int(input("""What type of file do you want to find?\n
        1 - Document, 2 - Video, 3 - Audio\n
        4 - Photo, 5 - Self-defined\n> """))
    if start == 1:
        f_type = "doc"
        print("\n")
        choice_find(f_type)

    elif start == 2:
        f_type = "vid"
        print("\n")
        choice_find(f_type)

    elif start == 3:
        f_type = "aud"
        print("\n")
        choice_find(f_type)

    elif start == 4:
        f_type = "img"
        print("\n")
        choice_find(f_type)

    elif start == 5:
        f_type = "usr"
        print("\n")
        choice_find(f_type)

    else:
        print("Please provide a number.\n\n\n")
        start_find()


def choice_find(f_type):
    if f_type == "doc":
        print("Searching for documents:")
        ext_list = open("Resources/documents.txt", "r")
        list_lines = ext_list.read().splitlines()
        f_name = input("What would you like to find?:\n> ")
        f_loc = input("Where do you want to search?:\n> ")
        name_type = [f_name + "." + line for line in list_lines]
        ext_list.close()
        results = []
        for item in name_type:
            results.append(glob.glob(f_loc + item, recursive=True))
        fil_results = list(filter(None, results))
        print(fil_results)

    elif f_type == "vid":
        print("Searching for videos:")
        ext_list = open("Resources/videos.txt", "r")
        list_lines = ext_list.read().splitlines()
        f_name = input("What would you like to find?:\n> ")
        f_loc = input("Where do you want to search?:\n> ")
        name_type = [f_name + "." + line for line in list_lines]
        ext_list.close()
        results = []
        for item in name_type:
            results.append(glob.glob(f_loc + item, recursive=True))
        fil_results = list(filter(None, results))
        print(fil_results)

    elif f_type == "aud":
        print("Searching for audio tracks:")
        ext_list = open("Resources/audio.txt", "r")
        list_lines = ext_list.read().splitlines()
        f_name = input("What would you like to find?:\n> ")
        f_loc = input("Where do you want to search?:\n> ")
        name_type = [f_name + "." + line for line in list_lines]
        ext_list.close()
        results = []
        for item in name_type:
            results.append(glob.glob(f_loc + item, recursive=True))
        fil_results = list(filter(None, results))
        print(fil_results)

    elif f_type == "img":
        print("Searching for images:")
        ext_list = open("Resources/images.txt", "r")
        list_lines = ext_list.read().splitlines()
        f_name = input("What would you like to find?:\n> ")
        f_loc = input("Where do you want to search?:\n> ")
        name_type = [f_name + "." + line for line in list_lines]
        ext_list.close()
        results = []
        for item in name_type:
            results.append(glob.glob(f_loc + item, recursive=True))
        fil_results = list(filter(None, results))
        print(fil_results)

    elif f_type == "usr":
        print("Searching for user defined extention:")
        f_name = input("What would you like to find?:\n> ")
        f_type = input("What type of file are you looking for?:\n> ")
        f_loc = input("Where do you want to search?:\n> ")
        results = []
        results.append(glob.glob(f_loc + f_name + f_type, recursive=True))
        fil_results = list(filter(None, results))
        print(fil_results)


start_find()
