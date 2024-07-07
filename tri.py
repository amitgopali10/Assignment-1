def print_triangle(rows):
    for i in range(1, rows + 1):
        print('*' * i)

def main():
    try:
        rows = int(input("Enter the number of rows for the triangle: "))
        
        print_triangle(rows)
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
