fname = input("Enter file name: ")
fh = open(fname)
sentence = list()
words = list()
for line in fh:
    line.rstrip()
    sentence = line.split()
    for word in sentence:
        if word not in words:
                words.append(word)

words.sort()
print(words)
