import os
from pathlib import Path

search = input("What would you like to find:\n> ")
results = []
for file_name in os.path.listdir:
    if search in file_name:
        results.append(file_name)

print(results)


# USE GLOB
