hrs = input('Enter Hours: ')
rate = input('Enter Rate: ')
# Use try/except to catch any problems a user may input
try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error, enter numeric input.")
    quit()  # Ends the program. Run program again to correct the inputs

# Any hours over 40 is 1.5 of rate
if h <= 40:
    pay = h * r
else:
    overtime = (h - 40) * (1.5 * r)
    pay = (40 * r) + overtime

print(pay)
