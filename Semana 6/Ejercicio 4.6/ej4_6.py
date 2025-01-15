def computepay (h1, r1):
    if h1 > 40:
        x = ((h1 - 40) * r1 * 1.5) + (40 * r1)
        return x

    else:
        x = h1 * r1
        return x


hrs = input("Enter Hours:")
rt = input("Enter Rate:")

h = float(hrs)
r = float(rt)

p = computepay (h, r)
print("Pay", p)
