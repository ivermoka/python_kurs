navn: str = input("Navn: ")

def function(navn: str) -> str:
    alder: int = int(input(f'Hei, {navn}. Hvor gammel er du? : '))
    bosted: str = input(f'Hvor bor du, {navn}? : ')
    return alder, bosted

alder, bosted = function(navn)

print(f'navn: {navn}, alder: {alder}, bosted: {bosted}')