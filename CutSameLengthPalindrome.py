def reverse(s):
    return s[::-1]

def isPalindrome(s):
    rev = reverse(s)

    if (s == rev):
        return True
    return False

a = "alpppha"
b = "tesssla"
for i in range(int(len(a)/2)):
    temp1 = a[:i+1]+b[i+1:]
    print(temp1)
    if(isPalindrome(temp1)):
        print("Exists")
        break
    temp2 = b[:i+1]+a[i+1:]
    print(temp2)
    if (isPalindrome(temp2)):
        print("Exists")
        break
