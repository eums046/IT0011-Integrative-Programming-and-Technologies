string = input("Enter a string: ")
vowels = consonants = spaces = others = 0

for char in string:
    if char.lower() in 'aeiou':
        vowels += 1
    elif char.isalpha():
        consonants += 1
    elif char == ' ':
        spaces += 1
    else:
        others += 1

print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")
print(f"Spaces: {spaces}")
print(f"Other characters: {others}")