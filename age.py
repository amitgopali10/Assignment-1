def classify_age(age):
    if age < 18:
        return "You are a minor."
    elif 18 <= age < 65:
        return "You are an adult."
    else:
        return "You are a senior."

def main():
    try:
        age = int(input("Please enter your age: "))
        if age < 0:
            print("Age cannot be negative. Please enter a valid age.")
        else:
            message = classify_age(age)
            print(message)
    except ValueError:
        print("Invalid input. Please enter a numeric value for age.")

if __name__ == "__main__":
    main()
