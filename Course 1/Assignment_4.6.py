def computepay(h,r):
    if h < 40:
        pay = h * r
        print (p)
    else:
        reg = 40 * r
        h = h - 40
        r = r * 1.5
        pay = reg + (h * r)
    return pay

hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")
h = float(hrs)
r = float(rate)

p = computepay(h,r)
print(p)
