import json

person = {"name": "John", "age": 30, "City": New York, "has children": False}

personJSON = json.dumps(person, indent=4, sort_keys=True)
print(personJSON)

with open('person.json', 'w') as file:
    json.dump(person, file, indent=4)
