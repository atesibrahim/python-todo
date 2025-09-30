contents = ["Hello, World!",
            "Python is great.",
            "Let's write some files."]

filenames = ['data1.txt', 'data2.txt', 'data3.txt']

for content, filename in zip(contents, filenames):
    file = open(f"../files/{filename}", 'w')
    file.write(content)