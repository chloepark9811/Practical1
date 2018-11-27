sales = float(input("Enter sales: $"))

if 0 < sales < 1000:
    bonus = sales * 0.1
    print("bonus: $", bonus)

elif sales >= 1000:
    bonus = sales * 0.15
    print("bonus: $", bonus)

else:
    print("Invalid")