import random
import time


rows = int(input("Antall rows: "))
columns = int(input("Antall columns: "))

liste = []

for i in range(rows):
    row = []  
    for j in range(columns):
        row.append(random.randint(0, 9))
    liste.append(row)  

def printBoard(currentList, currentIndex):
    for i in range(len(liste)):
        strRow = ""
        for j in range(len(liste[i])):
            if i == currentList and j == currentIndex:
                strRow += "🧍🏻"
            else:
                strRow += str(liste[i][j]) + "\t"
        print(strRow)

currentList = 0
currentIndex = 0
running = True
totalTurns = 0

def greedChecker(currentList, currentIndex, running, totalTurns):
    if currentList == rows - 1 and currentIndex == columns - 1:
        print("\033[92mFinished")
        print(f'Total turns for greed-bot: {totalTurns}')
        running = False
    else:
        totalTurns += 1

        rightValue = liste[currentList + 1][currentIndex] if currentList + 1 < rows else float('-inf')
        bottomValue = liste[currentList][currentIndex + 1] if currentIndex + 1 < columns else float('-inf')
        
        if rightValue > bottomValue:
            currentList += 1
        elif rightValue < bottomValue:
            currentIndex += 1
        else:
            print("Stuck")
            while currentList >= 0 and liste[currentList][currentIndex] == rightValue:
                currentList -= 1
            while currentIndex >= 0 and liste[currentList][currentIndex] == bottomValue:
                currentIndex -= 1
        time.sleep(0.5)
    return currentList, currentIndex, running, totalTurns

visited = [[False] * columns for _ in range(rows)]

while running:
    print("-------------")
    if visited[currentList][currentIndex]:
        print("Backtracking...")
        while visited[currentList][currentIndex]:
            currentIndex -= 1
            if currentIndex < 0:
                currentIndex = columns - 1
                currentList -= 1
            if currentList < 0:
                currentList = 0
                currentIndex = 0
        print("Backtracking complete.")
    visited[currentList][currentIndex] = True
    printBoard(currentList, currentIndex)
    currentList, currentIndex, running, totalTurns = greedChecker(currentList, currentIndex, running, totalTurns)
