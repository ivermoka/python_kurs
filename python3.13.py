def lønnRegner(timelønn: int, antallTimer: int) -> int:
    return timelønn * antallTimer

def returnerer() -> int:
    timelønn: int = int(input("Timelønn: "))
    antallTimer: int = int(input("Antall timer: "))

    lønn = lønnRegner(timelønn, antallTimer)
    return lønn, timelønn, antallTimer

lønn, timelønn, antallTimer = returnerer() 
print(f'Lønnen din er {lønn}, basert på timelønn gitt som {timelønn} og antall timer som {antallTimer}')