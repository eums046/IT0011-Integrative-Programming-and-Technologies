
# Activity 1: Condition

# 1. Create a program that will ask the user to enter three numbers and display which number is highest.
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a > b:
    if a > c:
        highest = a
    else:
        highest = c
else:
    if b > c:
        highest = b
    else:
        highest = c

print("The highest number is", highest)

print()
print()

# 2. Refer to problem number 1. Display the three numbers in descending order.
if a > b:
    if a > c:
        if b > c:
            first, second, third = a, b, c
        else:
            first, second, third = a, c, b
    else:
        first, second, third = c, a, b
else:
    if b > c:
        if a > c:
            first, second, third = b, a, c
        else:
            first, second, third = b, c, a
    else:
        first, second, third = c, b, a

print("Numbers in descending order:", first, second, third)
