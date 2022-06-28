def karatsuba(x, y):
    """
        result = (10^(n/2) * a + b) * (10^(n/2)c + d) = 10^n * ac + 10^(n/2) * (ad + bc) + bd;
        Step1: res1 = ac
        Step2: res2 = bd
        Step3: res3 = (a + b) * (c + d) = ac + ad + bc + bd
               ad + bc = res3 - ac - bd
        """
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x * y

    n = max(len(str(x)), len(str(y)))
    n2 = n // 2

    a = x // 10**n2
    b = x % 10**n2
    c = y // 10**n2
    d = y % 10**n2

    res1 = karatsuba(a, c)
    res2 = karatsuba(b, d)
    res3 = karatsuba((a + b), (c + d))

    return 10**(2*n2) * res1 + 10**n2 * (res3 - res1 - res2) + res2


print(karatsuba(3141592653589793238462643383279502884197169399375105820974944592,
                2718281828459045235360287471352662497757247093699959574966967627))
