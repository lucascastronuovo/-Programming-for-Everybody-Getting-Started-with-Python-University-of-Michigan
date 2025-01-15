sl = None
largest = None
smallest = None

while True:
    x = input("Enter a number: ")
    if x == "Done":
        print("Maximum is", largest)
        print("Minimum is", smallest)
        break
    try:
        y = int(x)

    except:
        print("Invalid input")
        continue

    if sl is None:
        sl = y
        largest = y
        smallest = y

    elif y > largest:
        largest = y

    elif y < smallest:
        smallest = y
