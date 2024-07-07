def fibonacci_series(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

def main():
    n = 10  
    series = fibonacci_series(n)
    print(f"The first {n} numbers of the Fibonacci series are:")
    for num in series:
        print(num, end=" ")

if __name__ == "__main__":
    main()
