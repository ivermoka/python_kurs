# Gjennomsnittsalderen til x antall mennesker 

def gjennomsnittMennesker():
    antallMennesker = int(input("Hvor mange mennesker? "))
    alderMennesker = 0
    i = 0
    
    while i < antallMennesker:
        userInput = float(input(f'Alder til menneske {i+1}: '))
        alderMennesker += userInput
        i += 1
    return float(alderMennesker / antallMennesker) 


print("Gjennomsnittsladeren til menneskene dine er: ", gjennomsnittMennesker())
