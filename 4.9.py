input: list = [5, 10, 134, 1283, 2]

def maxNum(liste: list):
    number = 0
    for index in liste:
        if index > number:
            number = index
    return number
print(maxNum(input))