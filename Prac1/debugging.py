score = float(input("Enter score: "))
if score > 100 or score < 0:
        print("Invalid score")
else:
    if score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
         print("Bad")
