feet_inches = input("Enter feet and inches (e.g., 5 10): ")

def parse(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return feet, inches

def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters

def convert_to_cm(feet, inches):
    total_inches = (feet * 12) + inches
    cm = total_inches * 2.54
    return cm

feet_inches_tuple = parse(feet_inches)
feet, inch = parse(feet_inches)
result = convert(feet_inches_tuple[0], feet_inches_tuple[1])
result = convert(feet, inch)
if result < 1:
    print(f"{result * 100:.2f} cm")
else:
    print(f"{result:.2f} m")