"""
CodingBat: sorta_sum
https://codingbat.com/prob/p116620

Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.
"""

def sorta_sum(a, b):
    if a + b >= 10 and a + b <= 19:
        return 20
    else:
        return a + b

# Tests
if __name__ == "__main__":
    print(sorta_sum(3, 4))
    print(sorta_sum(9, 4))
    print(sorta_sum(10, 11))