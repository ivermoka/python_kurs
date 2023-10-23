konti: dict = {

}

def legg_til_konti():
    konto = input("Konto navn: ")
    penger = float(input("Penger inn: "))
    konti.update({konto:penger})
    print("Ny konti: ")
    for key, value in konti.items():
        print(key, ":", value)
legg_til_konti()