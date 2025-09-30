filenames = ['1.data1.txt', '2.data2.txt', '3.data3.txt']
filenames_new = []
for index, filename in enumerate(filenames):
    filename = filename.replace('.', '-', 1)
    row = f"{index}{filename}"
    print(row)
    filenames_new.append(filename)
print(filenames_new)