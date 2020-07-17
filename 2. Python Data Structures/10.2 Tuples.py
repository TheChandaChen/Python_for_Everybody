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

#creates a list with the key/values from dictionary and sorts the list by hour(key)
hour_counter = list()
for hour, counter in sorted(count.items()):
    print(hour, counter)
