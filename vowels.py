def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    for char in input_string:
        if char in vowels:
            vowel_count += 1
    return vowel_count

def main():
    try:
        input_string = input("Enter a string: ")
        
        num_vowels = count_vowels(input_string)
        
        print(f"The number of vowels in '{input_string}' is: {num_vowels}")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
