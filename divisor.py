def division_handling(dividend, divisor):
    try:
        result = dividend / divisor
        return result
    except ZeroDivisionError:
        return "Error! Division by zero."

def main():
    try:
        dividend = float(input("Enter the dividend: "))
        divisor = float(input("Enter the divisor: "))
        
        result = division_handling(dividend, divisor)
        
        print(f"The result of {dividend} / {divisor} is: {result}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
