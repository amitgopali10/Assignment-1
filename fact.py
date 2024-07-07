# Import the custom module
import custom_module

def main():
    try:
        number = int(input("Enter a number to find its factorial: "))
        
        if number < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            result = custom_module.factorial(number)
            print(f"The factorial of {number} is {result}")
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
