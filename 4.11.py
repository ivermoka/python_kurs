temperatures: list = [30, 11, 2, -1, 15, 50, 9]
days: list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
wind: list = [14, 26, 18, 6, 2, 5, 1]
rain: list = [4, 28, 14, 8, 9, 2, 4]

for index in range(7):
    print(f'|{temperatures[index]} °C, {wind[index]} m/s wind, {rain[index]} m/s rain : {days[index]}')