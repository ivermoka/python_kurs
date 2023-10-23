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


def bank_tjeneste():
    running = True
    while running:
        bruker = input("Valg (ny konto, oppdatere saldo, !quit): ")
        if (bruker == "ny konto"):
            legg_til_konti()
        elif (bruker == "oppdatere saldo"):
            oppdater_saldo(input("Nøkkel: "), int(input("Verdi: ")))
        elif (bruker == "!quit"):
            print("quitting...")
            return
        else:
            print("Ugyldig input.")
bank_tjeneste()
