#Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.
numbers = 0
for _ in range(1, 11):
    num = float(input(f"Enter number {_}: "))
    odd_num = num % 2
    if odd_num != 0:
        numbers += 1

print(f"there are {numbers} odd numbers")