def spi(credits, grades):
    """
    Calculate the Semester Performance Index (SPI) which is the weighted mean of credits and grades.
    """
    if len(credits) != len(grades) or len(credits) == 0:
        print("Number of credits and grades do not match!")
        return None
    elif any(grade < 0 or grade > 10 for grade in grades):
        print("Invalid value of grades!")
        return None
    elif any(credit < 0 or credit > 4 for credit in credits):
        print("Invalid value of credits!")
        return None
    else:
        total = sum(credit * grade for credit, grade in zip(credits, grades))
        return total / sum(credits)


def cpi(spi_values, credits):
    """
    Calculate the Cumulative Performance Index (CPI) which is the weighted mean of SPI values and credits.
    """
    if len(credits) != len(spi_values):
        print("Number of credits and SPIs do not match!")
        return None
    elif not (1 <= len(credits) <= 8) or not (1 <= len(spi_values) <= 8):
        print("Invalid number of credits or SPIs!")
        return None
    elif any(credit < 0 for credit in credits):
        print("Invalid value of credits!")
        return None
    elif any(spi < 0 or spi > 10 for spi in spi_values):
        print("Invalid value of SPI!")
        return None
    else:
        total = sum(spi * credit for spi, credit in zip(spi_values, credits))
        return total / sum(credits)


# SPI Tests
def spi_tests():
    credits_tests = [
        [3, 3, 2, 3, 2],
        [3, 4, 3, 1, 2],
        [2, 3, 4, -2, 1],
        [3, 4, 2, 1],
        [1, 2, 3, 3, 2]
    ]
    grades_tests = [
        [10, 9, 6, 7, 8],
        [10, 6, 5, 8, 5],
        [5, 7, 5, 10, 9],
        [10, 4, 5, 6, 3],
        [2, 3, 4, 5, 7]
    ]
    
    for i in range(len(credits_tests)):
        print(f'Test {i + 1} - ', end="")
        try:
            spi_value = spi(credits_tests[i], grades_tests[i])
            if spi_value is not None:
                print(f"SPI: {round(spi_value, 2)}")
        except Exception as e:
            print(f"Error: {e}")
        print()  # Prints a newline


# CPI Tests
def cpi_tests():
    spi_tests = [
        [9.21, 9.32, 8.15, 8.65, 8.88, 8.92, 8.71, 9.00],
        [9.44, 9.28, 9.45, 8.73, 9.36, 8.84, 8.72, 9.49],
        [8.58, 8.56, 9.37, 9.27, 9.45, 8.53, 8.58],
        [9.3, 8.93, 9.12, 8.97, 9.03, 9.36, 8.64, 9.04]
    ]
    semester_credits_tests = [
        [22, 22, 23, 22, 24, 22, 23, 22],
        [22, 22, 24, 22, 23, 22, 23, 24],
        [22, 24, 22, 22, 22, 22, 24, 23],
        [23, 23, 22, 24, 24, 22, -23, 24]
    ]
    
    for i in range(len(spi_tests)):
        print(f"Test {i + 1} - ", end="")
        try:
            cpi_value = cpi(spi_tests[i], semester_credits_tests[i])
            if cpi_value is not None:
                print(f"CPI: {round(cpi_value, 2)}")
        except Exception as e:
            print(f"Error: {e}")
        print()  # Prints a newline


# Run the tests
spi_tests()
cpi_tests()
