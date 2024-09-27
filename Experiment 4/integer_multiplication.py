def normal_multiplication(x, y):
    """
    Performs multiplication of two integers by the normal method.
    """
    if type(x) == float or type(y) == float:
        print("Not an integer")
        return -1
    sign = -1 if (x < 0) ^ (y < 0) else 1
    x, y = abs(x), abs(y)

    x = str(x)[::-1]
    y = str(y)[::-1]
    res = 0
    for power1, digit1 in enumerate(x):
        for power2, digit2 in enumerate(y):
            res += int(digit1) * int(digit2) * 10 ** (power1 + power2)
    
    return sign*res


def karatsuba_multiplication(x, y):
    """
    Performs multiplication of two integers using the divide and conquer karatsuba algorithm.
    """
    if type(x) == float or type(y) == float:
        print("Not an integer")
        return -1
    sign = -1 if (x < 0) ^ (y < 0) else 1
    x, y = abs(x), abs(y)

    if x < 10 or y < 10:
        return x * y
    
    m = min( 
        len(str(x)), 
        len(str(y)) 
            )
    m2 = m//2
    
    high1, low1 = divmod(x, 10**m2)         # Equivalent to splitting in the middle
    high2, low2 = divmod(y, 10**m2)
    
    z0 = karatsuba_multiplication(low1, low2)
    z2 = karatsuba_multiplication(high1, high2)
    z1 = karatsuba_multiplication(low1 + high1 , low2 + high2) - z2 - z0
    # The function outputs low1*low2 + high1*low2 + high1*high2 + high2*low1
    # from which we must subtract low1low2(z0) and high1high2(z2)
    
    return sign * (z2*(10 ** (2*m2)) + z1*(10 ** m2) + z0)

def tests():
    numbers = [
        (12342342352354534553346356, 30456034568347603463563565),
        (53849450494776394611921152, -50633509739863107177770622), 
        (25069.51, 77777.321),
        (0, 1155328940683083679213231), 
        (97672243867560276084372410, 0), 
        (-2551817852586546680292533, 73441952913786780372193468.454), 
        (-74494213327602150702262607, -68674501952269147188782896), 
        (222.01, 0),
        (-444.05, 1000.001),
        (-36363636, 1515.15)
    ]

    for x,y in numbers:
        print(f"Testcase: {x}, {y}")
        print(normal_multiplication(x, y))
        print(karatsuba_multiplication(x, y))


tests()