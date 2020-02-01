from collections import namedtuple
def main():
    with open("data_person_1000000.csv","r",encoding="utf-8") as file:
        people_strings = file.read().splitlines()
    Person = nametuple("Person",people_strings[0])