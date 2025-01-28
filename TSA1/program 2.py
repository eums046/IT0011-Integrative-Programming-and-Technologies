string = input("Enter a string: ")
total = 0

for char in string:
    if char.isdigit():
        total += int(char)

print(f"Sum of digits: {total}")
