person = {'name': 'Alex', 'age': 17, 'drivers license': False, 'height': 175, 'sex': 'non-binary'}

person.pop('sex')
if 'height' in person:
    print("height in person")

print(person.keys())
print(person.values())