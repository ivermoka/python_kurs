
aksjekurs = {'EQNR': [233.90, 'equinor', 3700000], 'DNB': [210.50, 'dnb bank asa', 382664],
'NHY': [71.04, 'norsk hydro', 3300000], 'PMG': [18.52, 'play magnus', 26063]}
aksjeNavn = []

def aksjeNavnHenter():
    for i in aksjekurs:
        aksjeNavn.append(aksjekurs.get(i)[1].capitalize())
    return aksjeNavn

print(aksjeNavnHenter())