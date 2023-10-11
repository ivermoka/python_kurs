frukt = "banan" # definer global variabel


def fruktEndrer(): # funksjonen for å endre frukt
    frukt2 = "eple"
    frukt = frukt2
    return frukt

print(frukt)

frukt = fruktEndrer() # redefiner global variabel 

print(frukt)