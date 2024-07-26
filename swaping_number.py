num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))

print("***********************   Your Number   ******************************\n")
print("Your first number : ",num1,"\nYour second number : ",num2)
print("\n***********************   First method for Swaping Number   ******************************\n")

#First Method ....
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print("First number : ",num1,"\nSecond number : ",num2)

print("\n***********************   Your Number   ******************************\n")
print("Your first number : ",num1,"\nYour second number : ",num2)
print("\n***********************   Second method for Swaping Number   ******************************\n")

#Second method
num1 = num1 * num2
num2 = num1 / num2
num1 = num1 / num2

print("First number : ",num1,"\nSecond number : ",num2)
