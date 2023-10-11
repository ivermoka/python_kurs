
string = input("Skriv inn setningen din")
index = int(input("Skriv inn indexen din"))
bokstav = input("Skriv inn bokstaven som skal inn i setningen din")

print(string)

string = string[:index] + bokstav + string[index:]

print(string)