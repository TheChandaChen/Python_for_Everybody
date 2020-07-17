name = input("Enter file name: ")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

# creates a dictionary of hours and a count of the hours by doing multiple splits
count = dict()
for email in handle:
    if email.startswith("From "):
        words = email.split()
        time = words[5]
        split_time = time.split(':')
        hour = split_time[0]
        count[hour] = count.get(hour, 0) + 1

# sorts the dictionary items (tuples) and prints out the sorted hour and counter
for hour, counter in sorted(count.items()):   # sorted(count.items()) is a lsit of tuples
    print(hour, counter)
