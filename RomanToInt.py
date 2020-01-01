def romanToInt(x):
    a = {'(X)' : 10000, 'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    res = 0
    for i in range(0, len(x) - 1):
        if a[x[i]] < a[x[i + 1]]:
            res -= a[x[i]]
        else:
            res += a[x[i]]
    print(res + a[x[-1]])
    print()

romanToInt('CCXXII')