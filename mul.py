def multiplication_table(number):
    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i} = {result}")

def main():
    try:
        number = int(input("Enter a number to generate its multiplication table: "))
        
        multiplication_table(number)
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
