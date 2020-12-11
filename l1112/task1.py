def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def lcm(a, b):
    res = a * b // gcd(a, b)
    return res


print(lcm(3, 5))

