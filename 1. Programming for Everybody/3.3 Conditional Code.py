score = input("Enter Score: ")
# try/except tests if user input is a numeric number
try:
    s = float(score)
except:
    print("Error, input numeric number.")
    quit()

# tests if the input is between 0 and 1
if s > 1:
    print("Error, input number between 0 and 1.")
    quit()
elif s < 0:
    print("Error, input number between 0 and 1.")
    quit()

# prints out letter grade based on score
if s >= 0.9:
    print("A")
elif s >= 0.8:
    print("B")
elif s >= 0.7:
    print("C")
elif s >= 0.6:
    print("D")
else:
    print("F")
