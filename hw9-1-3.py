# Author: CCG 1/12/22

def find_thing(file, substring):
    for index, value in enumerate(file):
        if value == substring:
            print(index)
            break
        if substring not in file:
            print("-1")

find_thing("slam", "a")
