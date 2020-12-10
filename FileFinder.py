# import os
import glob  # glob is used for searching
# from pathlib import Path

file_search = input("What would you like to find:\n> ")
file_type = input("What type of file are you looking for:\n> ")
file_location = input("If you know the rough location let me know:\n> ")
string = str(file_location + file_search + file_type)
result = glob.glob(f"{string}", recursive=False)
print(result)
