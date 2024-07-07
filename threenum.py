def check_sum(a, b, c):
    return a + b == c

def main():
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        c = float(input("Enter the third number: "))
        
        if check_sum(a, b, c):
            print(f"{c} is the sum of {a} and {b}.")
        else:
            print(f"{c} is not the sum of {a} and {b}.")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
