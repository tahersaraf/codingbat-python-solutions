"""
CodingBat: diff21
https://codingbat.com/prob/p197466

Given an int n, return the absolute difference between n and 21, 
except return double the absolute difference if n is over 21.
"""

def diff21(n):
    if n > 21:
        return 2*(n - 21)
    else:
        return 21 - n

# Tests
if __name__ == "__main__":
    print(diff21(19))  # 2
    print(diff21(10))  # 11
    print(diff21(21))  # 0
    print(diff21(22))  # 2
    print(diff21(25))  # 8