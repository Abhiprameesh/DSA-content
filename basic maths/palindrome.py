#A palindrome is a number that reads the same backward as forward. For example, 121, 1331, and 4554 are palindromes because they remain the same when their digits are reversed.
n = input("Enter a value: ")#user input in string format
reverse_num = n[::-1]#reverse the string using slicing
if n == reverse_num:
    print("The number is a palindrome.")    
else:
    print("The number is not a palindrome.")
