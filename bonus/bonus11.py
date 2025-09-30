def get_average():
    with open('../files/data.txt', 'r') as file:
        numbers = file.readlines()

    values = numbers[1:]
    values = [float(i) for i in values]

    average = sum(values) / len(values)

    return average


average = get_average()
print(average)