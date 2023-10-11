string = input("String: ")

def split(word):
    return list(word)

vokaler = ['a', 'e', 'i', 'o', 'u', 'y', 'æ', 'ø', 'å']

string = split(string)
print(string)

def letterChecker():
    for letter in string:
        if (letter in vokaler):
            print(f'{letter} er en vokal')
            return True
        
isVokal = letterChecker()

if (isVokal != True):
    print("ordet inneholder ikke en vokal.")

    
