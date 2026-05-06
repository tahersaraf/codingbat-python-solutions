"""
CodingBat: makes10
https://codingbat.com/prob/p124984


Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.
"""

def makes10(a, b):
    return (a==10 or b==10) or (a+b==10)

# Tests
if __name__ == "__main__":
    print(makes10(9, 10))  # True
    print(makes10(9, 9))   # False
    print(makes10(1, 9))   # True
    print(makes10(10, 1))  # True
    print(makes10(10, 10)) # True