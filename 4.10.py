liste: list = []

running = True
while running:
    userInput = input("NUMBER/!stop: ")
    if (userInput == "!stop"):
        running = False
    else:
        liste.append(float(userInput))

for i in range(len(liste)):
    liste[i] = float(liste[i])
print(sum(liste))


