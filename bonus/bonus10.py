try:
    width = float(input("Enter the width: "))
    height = float(input("Enter the height: "))
    if width == height:
        exit("The width and height can't be equal.")

    area = width * height
    print(area)
except ValueError:
    print("Invalid input. Please enter numeric values for width and height.")