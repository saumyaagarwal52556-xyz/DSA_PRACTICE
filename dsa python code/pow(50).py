def myPow(x,n):
    if n <0:
        x = 1/x
        n = -n

    curr = x
    result = 1

    while n > 0:
        if n % 2 != 0:
            result *= curr
        curr *= curr

        n //= 2

    return result