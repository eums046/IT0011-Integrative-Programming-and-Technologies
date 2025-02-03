# 1. Create a program that will compute the sum of the numbers from 1st term up to the last term input by the user.

first_term = int(input("Enter first term number: "))
last_term = int(input("Enter last term number: "))

total_sum = 0

for number in range(first_term, last_term + 1):
    total_sum += number

print(f"The sum of the numbers from {first_term} to {last_term} is {total_sum}")

print()
print()

#2. Create a program will show if the given input number is a prime number (a whole number greater than 1 that cannot be exactly divided by any whole number other than itself and 1 e.g. 2, 3, 5, 7, 11). Use looping statement to solve the problem.
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

num = int(input("Enter a number: "))

if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")