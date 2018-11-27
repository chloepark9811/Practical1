print("Welcome to shop calculator")
num = int(input("Enter the number of items>>>"))
while num<0:
    print("Invalid value. Please enter positive value only")
    num = int(input("Enter the number of items>>>"))
total = 0.0
for i in range(1, num+1, 1):
    price = float(input("Enter price for item"))
    print("Price: $", price)
    total += price
if total >= 100:
    total = total-total*0.1
    print("Total: $", total)
else:
    print("Total: $", total)