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