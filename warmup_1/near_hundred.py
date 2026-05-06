"""
CodingBat: near_hundred
https://codingbat.com/prob/p124676

Given an int n, return True if it is within 10 of 100 or 200. 
Note: abs(num) computes the absolute value of a number.
"""

def near_hundred(n):
    return bool(abs(100 - n) <= 10 or abs(200 - n) <= 10)

# Tests
if __name__ == "__main__":
    print(near_hundred(93))  # True
    print(near_hundred(90))  # True
    print(near_hundred(89))  # False
    print(near_hundred(110)) # True
    print(near_hundred(111)) # False
    print(near_hundred(121)) # False
    print(near_hundred(-101))# False