from collections import namedtuple
prom pprint import pprint
from searching import binary_search

processors = [
    str,
    str,
    float,
    int,
    str
]
def process_data(processors,data):
    for processor, item in zip(processors,data)
        yield processor(item)

def main():
    with open("datasets\data_person_1000000.csv","r",encoding="utf-8") as file:
        people_strings = file.read().splitlines()
    Person = nametuple("Person",people_strings[0])
    people = []
    for p in people_strings[1:20]:
        person_data = p.split(",")
        processed = process_data(procesors,person_data)
        people.append(Person(*processed))
    def simple_comparison(person):
        return person
    def first_name_comparison(person):
        return person.first