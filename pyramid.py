def print_pyramid(rows):
    for i in range(1, rows + 1):
        print(' ' * (rows - i), end='')
        print('*' * (2 * i - 1))

def main():
    try:
        rows = int(input("Enter the number of rows for the pyramid: "))
        
        print_pyramid(rows)
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
