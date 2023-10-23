liste: list = [5, 10, 134, 1283, 2]

number = 0
for index in liste:
    if index > number:
        print(f'{index} vs {number}')
        number = index
print(f'{number} wins!')