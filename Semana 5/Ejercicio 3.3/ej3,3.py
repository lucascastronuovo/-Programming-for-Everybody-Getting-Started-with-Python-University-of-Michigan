score = input("Enter Score: ")
try:
    s = float(score)
except:
    print("Error, please enter numeric number")
    quit()
if s > 1.0:
    print("Error")
elif s < 0.0:
    print("Error")
elif s >= 0.9:
    print("A")
elif s >= 0.8:
    print("B")
elif s >= 0.7:
    print("C")
elif s >= 0.6:
    print("D")
elif s < 0.6:
    print("F")
