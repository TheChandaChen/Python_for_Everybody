name = input("Enter file name: ")
handle = open(name)

count = dict()
for line in handle:
    line = line.rstrip()
    if line.startswith("From "):   # Need the space after "From" or it counts twice b/c of "From:"
        words = line.split()
        email = words[1]
        count[email] = count.get(email, 0) + 1

bigword = None
bigcount = None
for word, count in count.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)
