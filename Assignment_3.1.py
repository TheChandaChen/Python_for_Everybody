hrs = input('Enter Hours: ')
rate = input ('Enter Rate: ')
h = float(hrs)
r = float (rate)
if h < 40:
    pay = h * r
    print (pay)
else:
    reg = 40 * r
    h = h - 40
    r = r * 1.5
    pay = p + (h * r)
    print (pay)
