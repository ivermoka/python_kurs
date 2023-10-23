konti: dict = {}

def vis_konti():
    print("Konti: ")
    for key, value in konti.items():
        print(key, ":", value)
def legg_til_konti():
    konto = input("Konto navn: ")
    penger = float(input("Penger inn: "))
    konti.update({konto:penger})
    vis_konti()

def oppdater_saldo(nokkel, verdi):
    konti[nokkel] = verdi
    vis_konti()

legg_til_konti()
oppdater_saldo(input("Nøkkel: "), int(input("Verdi: ")))
