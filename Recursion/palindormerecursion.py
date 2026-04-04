def is_palindrome(s, i, j):
    if s[i] != s[j]:
        return False
    if i >= j:
        return True  
     
    # recursive call
    return is_palindrome(s, i + 1, j - 1)
s = input("Enter a string: ")
print(is_palindrome(s, 0, len(s) - 1))