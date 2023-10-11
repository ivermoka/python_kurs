amountOfIterations = int(input("Amount of iterations: "))

def iterator():
    global amountOfIterations

    for i in range (0, amountOfIterations):
        print("Hello World!")

iterator()