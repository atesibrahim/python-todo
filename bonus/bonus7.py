filenames = ['1.doc', '2.report', '3.presentation']

filenames = [filename.replace('.', '-') + '.txt' for filename in filenames]

print(filenames)

user_entries = ['10', '19.1', '20']

nums = [float(num) for num in user_entries]

sum = 0
for num in nums:
    sum += num
print(sum)