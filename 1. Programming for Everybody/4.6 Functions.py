# computepay is computing the user's pay
def computepay(h, r):
    if h <= 40:
        pay = h * r
        return pay
    else:
        overtime = (h - 40) * (1.5 * r)
        pay = (40 * r) + overtime
        return pay


hrs = input('Enter Hours: ')
rate = input('Enter Rate: ')

# Use try/except to catch any problems a user may input
try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error, enter numeric input.")
    quit()   # Ends the program. Run program again to correct the inputs

p = computepay(h, r)
print("Pay", p)
