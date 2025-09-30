member = input("Enter new member name: ")
with open("../files/members.txt", "a") as file:
    file.write(member + "\n")
print(f"Member '{member}' added to members.txt")

filenames = ['doc.txt', 'report.txt', 'presentation.txt']
for item in filenames:
    with open(f"../files/{item}.txt", "a") as file:
        file.write("Hello\n")

data1File = open("../files/data1.txt", "r")
content = data1File.read()
print(content)
data1File.close()

data2File = open("../files/data2.txt", "r")
content = data2File.read()
print(content)
data2File.close()

data3File = open("../files/data3.txt", "r")
content = data3File.read()
print(content)
data3File.close()