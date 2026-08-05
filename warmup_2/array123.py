"""
CodingBat: array123
https://codingbat.com/prob/p193604

Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.
"""

def array123(nums):
    if len(nums) >= 3:
        for i in range(len(nums)-1):
            if nums[i] == 1 and nums[i+1]==2 and nums[i+2]==3:
                return True
    return False

# Tests
if __name__ == "__main__":
    print(array123([1, 1, 2, 3, 1]))
    print(array123([1, 1, 2, 4, 1]))
    print(array123([1, 1, 2, 1, 2, 3]))