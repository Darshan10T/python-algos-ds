def reverseInt(x):
    if x > 0:
        y = int(str(x)[::-1])
    #for negative int
    if x <= 0:
        y = -1 * int(str(x * -1)[::-1])
    print(y)

reverseInt(-546)