def intToRoman(x):
    values = [10000, 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    numerals = ["(X)", "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    res = ""
    for i, j in enumerate(values):
        res += (x // j) * numerals[i]
        x %= j
    print(res)
    print()
intToRoman(10201)
