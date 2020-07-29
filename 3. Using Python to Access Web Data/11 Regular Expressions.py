import re

fname = input("Enter file name: ")
fh = open(fname)

num = 0

for line in fh:
    number = re.findall('[0-9]+', line)
    for onenum in number:
        onenum = int(onenum)
        num = num + onenum

print(num)
