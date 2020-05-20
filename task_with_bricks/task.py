def makeBricks(a, b, n):
    if n > a + b * 5:
        return False
    else:
        return n % 5 <= a
