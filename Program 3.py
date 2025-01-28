
rows = 5
print("a. ")
for i in range(1, rows + 1):
    print(" " * (rows * 2 - i * 2), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print()
print()

print("b. ")
line = 1
while line <= 5:
    if line <= 3:
        num = 2 * line - 1
    else:
        num = line + 2
    count = num

    printed = 0
    while printed < count:
        print(num, end="")
        printed += 1
    print()  
    
    line += 1