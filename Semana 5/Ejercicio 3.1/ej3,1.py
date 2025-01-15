hrs = input("Enter Hours:")
h = float(hrs)
rtfh = input("Enter Rate for Hours:")
r = float(rtfh)

if h > 40:
    pay = (h - 40) * r * 1.5 + (40 * r)
    print(pay)
else:
    pay = h * r
    print(pay)
