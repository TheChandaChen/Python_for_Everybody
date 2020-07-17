# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0.0
added = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    s = line.find(' ')
    num = line[s: ]
    num = num.lstrip()
    fnum = float(num)
    added = added + fnum

print("Average spam confidence:", added/count)
