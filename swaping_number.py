num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))

print("***********************   Your Number   ******************************\n")
print("Your first number : ",num1,"\nYour second number : ",num2)
print("\n***********************   Swapped Number   ******************************\n")

#First Method ....
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print("Your first number : ",num1,"\nYour second number : ",num2)