
string = input("Skriv inn setningen din")
index = int(input("Skriv inn indexen din"))
bokstav = input("Skriv inn bokstaven som skal inn i setningen din")

print(string)

liste = [1, 2, 3, 4]

liste = liste[:index] + bokstav + liste[index:]

print(string)