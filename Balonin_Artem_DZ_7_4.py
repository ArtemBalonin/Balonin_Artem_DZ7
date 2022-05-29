import os

folder = "."
dictionary = {}
for root, dirs, files in os.walk(folder):
    for file in files:
        size = os.stat(os.path.join(root, file)).st_size
        key = 10 ** len(str(size))
        if key in dictionary:
            dictionary[key] += 1
        else:
            dictionary[key] = 1
for key, value in sorted(dictionary.items()):
    print(f"{key}: {value} ")