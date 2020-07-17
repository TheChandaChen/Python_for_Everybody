#Use the file name words.txt
fname = input("Enter file name: ")

#ensures file name is typed in properly and exists
try:
    fh = open(fname)
except:
    print("File cannot be opened")
    quit()

#removes whitespace/newlines and capitalizes all characters
for lines in fh:
    lines = lines.rstrip()
    lines = lines.upper()
    print(lines)
