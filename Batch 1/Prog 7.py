#Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.
total = 0
for num in range(10):
    numbers = int(input(f"input number {num + 1}: "))
    total += numbers
print(total)