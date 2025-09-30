from unicodedata import digit

password = input("Enter the password: ")
result = {}

if len(password) >= 8:
    result["password length >= 8: "] = True
else:
    result["password length >= 8: "] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True
result["password contains digit: "] = digit

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True
result["password contains an uppercase: "] = uppercase

print(result)

if all(result.values()):
    print("Password is valid.")
else:
    print("Password is invalid.")