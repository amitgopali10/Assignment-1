def decimal_to_binary(n):
    if n == 0:
        return "0"
    binary_num = ""
    while n > 0:
        binary_num = str(n % 2) + binary_num
        n = n // 2
    return binary_num

def main():
    try:
        decimal_number = int(input("Enter a decimal number: "))
        if decimal_number < 0:
            print("Please enter a non-negative integer.")
        else:
            binary_number = decimal_to_binary(decimal_number)
            print(f"The binary equivalent of {decimal_number} is {binary_number}.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
