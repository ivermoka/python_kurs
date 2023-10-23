temperaturer: dict = {
    "bergen": "-20 °C",
    "oslo": "20 °C",
    "stavanger": "15 °C"
}
running = True
while running:
    user = input("by/!quit: ")
    if (user == "by"):
        newCity = input("By: ")
        newTemp = input("Temperatur: ")
        temperaturer.update({newCity: newTemp+" °C"})
    else:
        running = False
print("Temperaturer: ")
for key, value in temperaturer.items():
    print(key, value)