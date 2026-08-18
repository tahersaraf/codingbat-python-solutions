"""
CodingBat: has23
https://codingbat.com/prob/p177892

Given an int array length 2, return True if it contains a 2 or a 3.
"""

def has23(nums):
    return (2 in nums or 3 in nums)

# Tests
if __name__ == "__main__":
    print(has23([2, 5]))
    print(has23([4, 3]))
    print(has23([4, 5]))