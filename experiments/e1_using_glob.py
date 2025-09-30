import glob

myfiles = glob.glob("files/*.txt")

for filpath in myfiles:
    with open(filpath, "r") as file:
        print(file.read())

