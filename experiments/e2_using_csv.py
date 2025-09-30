import csv

with open("../files/weather.csv", "r") as file:
    data = list(csv.reader(file))

city = input("Enter city:")
for row in data:
    if row[0].lower() == city.lower():
        print(f"The temperature in {row[0]} is {row[1]}°C")
        break