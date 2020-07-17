#Use the file name romeo.txt
fname = input("Enter file name: ")
fh = open(fname)
words = list()   # Creates an empty list for the words

# for each line, remove whitespace and split the words up
for line in fh:
    line.rstrip()
    sentence = line.split()
    # for each word, if it's not in the words list, append it to the list
    for word in sentence:
        if word not in words:
            words.append(word)

words.sort()   # sorts the words list alphabetically
print(words)
