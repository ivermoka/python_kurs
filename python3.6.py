antallMennesker = int(input("Antall mennesker: "))
totalverdi: int = 0
def gjennomsnittRegner() -> int:
    global antallMennesker, totalverdi

    for i in range(1, antallMennesker + 1):
        menneske = int(input(f'Menneske {i} alder: '))
        totalverdi += menneske
    
    return totalverdi / antallMennesker

totalverdi = gjennomsnittRegner()
print(totalverdi)