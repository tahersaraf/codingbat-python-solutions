"""
CodingBat: love6
https://codingbat.com/prob/p100958

The number 6 is a truly great number. Given two int values, a and b, return True if either one is 6. Or if their sum or difference is 6. Note: the function abs(num) computes the absolute value of a number.
"""

def love6(a, b):
    return (a==6 or b==6) or ((a + b) == 6) or (abs(a - b) == 6)
    

# Tests
if __name__ == "__main__":
    print(love6(-7, 1))
    print(love6(4, 5))
    print(love6(1, 5))