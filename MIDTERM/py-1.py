with open('numbers.txt', 'r') as file:
    for line_num, line in enumerate(file, start=1):
        line = line.strip()
        if not line:
            continue
        numbers = line.split(',')
        try:
            sum_num = sum(int(num.strip()) for num in numbers)
        except ValueError:
            print(f"Line {line_num}: Invalid data in line")
            continue
        sum_str = str(sum_num)
        is_palindrome = sum_str == sum_str[::-1]
        status = "Palindrome" if is_palindrome else "Not a palindrome"
        print(f"Line {line_num}: {line} (sum {sum_num}) - {status}")