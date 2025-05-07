#Prog01: Create a program that ask user to input 2 numbers. Print the bigger number.
num1 = float(input("input number: "))
num2 = float(input("input number: "))

if num1 > num2:
    print(f"{num1} is greater than {num2}")
else:
    print(f"{num2} is greater than {num1}")