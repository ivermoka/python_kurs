string: str = input("Stringen din: ")
iSetning = ""

def sjekker(string: str, iSetning: str):
    '''
    SJEKKE OM Æ Ø Å ER I STRING
    '''
    bokstaver = ['æ', 'ø', 'å']

    for index in bokstaver:
        if (index in string):
            iSetning += index + ", "
    if (iSetning != ""):
        print(f'{iSetning}er i setningen {string}')
        

sjekker(string, iSetning)