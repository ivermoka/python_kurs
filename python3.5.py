timelønn = int(input("timelønn: "))
antallTimer = int(input("antall timer: "))

def lønnRegner(timelønn, antallTimer) -> int:
    return timelønn * antallTimer

print(f'Lønn: {lønnRegner(timelønn, antallTimer)}')