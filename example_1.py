data = [
    {
    "name": "piotr",
    "city": "warsaw",
    "age": 37,
    "hobbies": ["js", "python", "drugs"]
},
    {
    "name": "maciek",
    "city": "warsaw",
    "age": 25,
    "hobbies": ["bike", "books", "drugs"]
},
    {
    "name": "kon_rafal",
    "city": "raciborz",
    "age": 20,
    "hobbies": ["comics", "art", "literature"]
},
    {
    "name": "jedrek",
    "city": "poniatow",
    "age": 20,
    "hobbies": ["figurki", "skateboarding", "theatre"]
},
]


def count_unique_hobbies(people):
    hobbies = set()

    for person in people:
        hobbies |= set(hobby.lower() for hobby in person['hobbies'])

    return  len(hobbies)

count_unique_hobbies(data)


