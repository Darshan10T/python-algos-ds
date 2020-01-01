def isPalindrome(x) -> bool:
    return str(x) == str(x)[::-1]

print(isPalindrome(121))