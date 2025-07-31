def calculator():
    print("🧮 Python Calculator 🧮")
    print("Operations: + (Add), - (Subtract), * (Multiply), / (Divide), % (Modulus)")
    
    try:
        # Get user input
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        op = input("Enter operation (+, -, *, /, %): ").strip()
        
        # Perform calculation
        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                print("Error: Division by zero is impossible!")
                return
            result = num1 / num2
        elif op == '%':
            if num2 == 0:
                print("Error: Modulo by zero is undefined!")
                return
            result = num1 % num2
        else:
            print("Error: Invalid operation! Please use +, -, *, /, or %")
            return
        
        # Display result (removes .0 for whole numbers)
        if result.is_integer():
            result = int(result)
        print(f"\n{num1} {op} {num2} = {result}")
    
    except ValueError:
        print("Error: Please enter valid numbers!")

# Run the calculator
if __name__ == "__main__":
    calculator()