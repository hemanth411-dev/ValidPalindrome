from solution import Solution  

def main():
    solution = Solution()

    input_string = input("Enter a string to check if it's a palindrome: ")

    result = solution.isPalindrome(input_string)
    
    if result:
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")


if __name__ == "__main__":
    main()
