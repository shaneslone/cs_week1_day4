def csReverseIntegerBits(n):
    b = bin(n)[2:]
    output = b[::-1]
    return int(output, 2)

