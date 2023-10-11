def sammensetter() -> str:
    fornavn: str = input("Fornavn: ")
    etternavn: str = input("Etternavn: ")
    return fornavn + " " + etternavn

sammensattNavn = sammensetter()
print(sammensattNavn)