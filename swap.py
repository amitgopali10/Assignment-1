# Function to swap values of two variables
def swap_values(a, b):
    print(f"Before swapping: a = {a}, b = {b}")
    # Swapping without using a third variable
    a = a + b
    b = a - b
    a = a - b
    print(f"After swapping: a = {a}, b = {b}")

def main():
    try:
        a = int(input("Enter the value of a: "))
        b = int(input("Enter the value of b: "))
        
        swap_values(a, b)
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
