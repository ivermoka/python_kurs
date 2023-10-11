string: str = input("String: ")
index: int = int(input("Index: "))
bokstav: str = input("Bokstav: ")

def bokstavPlasserer(string: str, index: int, bokstav: str) -> str:
    """
    PLACE LETTER ON INDEX

    string
        your string

    index
        where the letter is placed
    
    bokstav
        the letter
    """ 
    return string[:index] + bokstav + string[index:] 

print(bokstavPlasserer(string, index, bokstav))