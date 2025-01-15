hrs = input("Enter Hours:")
rtfh = input("Enter Rate for Hours:")
try:
    h = float(hrs)
    r = float(rtfh)
except:
    print("Error, please enter numeric input")
    quit()


if h > 40:
    pay = (h - 40) * r * 1.5 + (40 * r)
    print(pay)
else:
    pay = h * r
    print(pay)
