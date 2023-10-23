liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(liste)
liste[4] = "hei"
print(liste)
liste.append("slutten")
print(liste)
liste.insert(4, "hei2")
del liste[0]
liste.pop()
print(liste)