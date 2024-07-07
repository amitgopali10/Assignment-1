def find_max_value(nums):
    if not nums:
        return None  
    
    max_value = nums[0]
    for num in nums[1:]:
        if num > max_value:
            max_value = num
    
    return max_value

def main():
    try:
        nums = input("Enter a list of numbers separated by space: ").split()
        nums = list(map(float, nums))  
        max_value = find_max_value(nums)
        
        if max_value is not None:
            print(f"The maximum value in the list is: {max_value}")
        else:
            print("The list is empty.")
    except ValueError:
        print("Invalid input. Please enter numeric values separated by space.")

if __name__ == "__main__":
    main()
