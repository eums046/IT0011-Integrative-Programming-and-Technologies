def divide(a, b):
    """
    Divides a by b. Returns None if b is zero.
    """
    if b == 0:
        print("Error: Cannot divide by zero.")
        return None
    return a / b

def exponentiate(a, b):
    """
    Raises a to the power of b.
    """
    return a ** b

def remainder(a, b):
    """
    Returns the remainder when a is divided by b. Returns None if b is zero.
    """
    if b == 0:
        print("Error: Cannot calculate remainder with zero divisor.")
        return None
    return a % b

def summation(a, b):
    """
    Returns the sum of all integers from a to b (inclusive).
    Returns None if b is less than a.
    """
    if b < a:
        print("Error: Second number must be greater than or equal to first number.")
        return None
    
    total = 0
    for i in range(a, b + 1):
        total += i
    return total

def main():
    while True:
        print("\n===== Mathematical Operations Menu =====")
        print("[D] - Divide")
        print("[E] - Exponentiation")
        print("[R] - Remainder")
        print("[F] - Summation")
        print("[Q] - Quit")
        
        choice = input("\nEnter your choice: ").upper()
        
        if choice == 'Q':
            print("Exiting program. Goodbye!")
            break
        
        if choice not in ['D', 'E', 'R', 'F']:
            print("Invalid choice. Please try again.")
            continue
        
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == 'D':
                result = divide(num1, num2)
            elif choice == 'E':
                result = exponentiate(num1, num2)
            elif choice == 'R':
                result = remainder(num1, num2)
            elif choice == 'F':
                # For summation, ensure the inputs are integers
                result = summation(int(num1), int(num2))
            
            if result is not None:
                print(f"Result: {result}")
        
        except ValueError:
            print("Error: Please enter valid numbers.")

if __name__ == "__main__":
    main()
