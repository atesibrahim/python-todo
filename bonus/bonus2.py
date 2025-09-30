password = input("Enter the password: ")

while password != "pass123":
    print("Incorrect password. Try again.")
    password = input("Enter the password: ")

print(password.upper())
print("Access granted.")

x = 1

while x <= 5:
    print(x)
    x += 1