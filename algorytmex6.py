import random
import time


rows = int(input("Antall rows: "))
columns = int(input("Antall columns: "))

liste = []

for i in range(rows):
    row = []  
    for j in range(columns):
        if random.randint(1, 4) == 1 and j != 0 and i != 0 and i < (rows-1) and j < (rows-1): 
            row.append("X")
        else:
            row.append(random.randint(0, 9))
    liste.append(row)  

def printBoard(currentList, currentIndex):
    for i in range(len(liste)):
        strRow = ""
        for j in range(len(liste[i])):
            if i == currentList and j == currentIndex:
                strRow += "🧍🏻\t"
            else:
                strRow += str(liste[i][j]) + "\t"
        print(strRow)

currentList = 0
currentIndex = 0
running = True
totalTurns = 0
totalPoints = 0

def greedChecker(currentList, currentIndex, running, totalTurns, totalPoints):
    points = 0
    if currentList == rows - 1 and currentIndex == columns - 1:
        print("\033[92mFinished")
        print(f'Total turns for greed-bot: {totalTurns}')
        running = False
    else:
        rightValue = liste[currentList][currentIndex + 1] if currentIndex + 1 < columns else float('-inf')
        bottomValue = liste[currentList + 1][currentIndex] if currentList + 1 < rows else float('-inf')
        print("right: ", rightValue, "bottom: ", bottomValue)

        if rightValue == "X" and bottomValue == "X":
            print("I lost.")
            running = False
            return currentList, currentIndex, running, totalTurns, totalPoints

        totalTurns += 1
        points += liste[currentList][currentIndex]
        totalPoints += points
        currentPosPoints = liste[currentList][currentIndex]

        print(f'Total turns: {totalTurns}. Total points: {totalPoints}. Current position points: {currentPosPoints}')

        if rightValue == "X":
            currentList += 1
            print("x. moving bottom")
        elif bottomValue == "X":
            currentIndex += 1
            print("x. moving right")
        elif rightValue < bottomValue and bottomValue != "X":
            currentList += 1
            print("moving bottom")
        elif rightValue > bottomValue and rightValue != "X":
            currentIndex += 1
            print("moving right")
        elif rightValue == bottomValue:
            currentIndex += 1
            print("same values. moving right.")

        time.sleep(0.5)
    return currentList, currentIndex, running, totalTurns, totalPoints



while running:
    print("-------------")
    printBoard(currentList, currentIndex)
    currentList, currentIndex, running, totalTurns, totalPoints = greedChecker(currentList, currentIndex, running, totalTurns, totalPoints)
