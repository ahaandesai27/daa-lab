def normal_multiplication(x: int, y: int) -> int:
    """
    Performs multiplication of two integers by the normal method.
    """
    x = str(x)[::-1]
    y = str(y)[::-1]
    res = 0
    for power1, digit1 in enumerate(x):
        for power2, digit2 in enumerate(y):
            res += int(digit1) * int(digit2) * 10 ** (power1 + power2)
    
    return res


def karatsuba_multiplication(x: int, y: int) -> int:
    """
    Performs multiplication of two integers using the divide and conquer karatsuba algorithm.
    """
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
    
    return z2*(10 ** (2*m2)) + z1*(10 ** m2) + z0

def tests():
    numbers = [
        (12342342352354534553346356, 30456034568347603463563565),
        (53849450494776394611921152, -50633509739863107177770622), 
        (87030377504722696254067401, 91108548674911341289250429), 
        (-25512918230620960054612468, 73446328940683083679212533), 
        (-83728178525865466802919907, 30661952913786780372194477), 
        (63006034979614442008301215, 74691341210634741645245499), 
        (-74494213327602150702262607, -68674501952269147188782896), 
        (97672243867560276084372410, 44739806469336357714097047), 
        (28071758192663907983471595, 55188420653766309645635066), 
        (15751086497362612912659415, 51047850892628130726509784)
    ]

    x,y = numbers[0]
    karatsuba_result = karatsuba_multiplication(x,y)
    normal_result = normal_multiplication(x,y)
    assert karatsuba_result == normal_result
    print(karatsuba_result)
    print(normal_multiplication(x,y))


tests()