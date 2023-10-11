tekst = 'Uten mat og drikke, duger helten ikke'
vokaler = 'aeiouyæøå'

for letter in tekst:
    if letter in vokaler:
        print("vokal: ", letter)
    else:
        print("konsonant: ", letter)
