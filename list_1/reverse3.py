"""
CodingBat: reverse3
https://codingbat.com/prob/p192962

Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.
"""

def reverse3(nums):
    return nums[::-1]

# Tests
if __name__ == "__main__":
    print(reverse3([1, 2, 3]))
    print(reverse3([5, 11, 9]))
    print(reverse3([7, 0, 0]))