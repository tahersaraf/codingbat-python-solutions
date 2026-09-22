"""
CodingBat: sum13
https://codingbat.com/prob/p167025  

Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
"""

def sum13(nums):
    sum = 0
    skip = False
    for i in range(len(nums)):
        if skip:
            skip = False
            continue
        if nums[i] == 13:
            skip = True
            continue
        sum += nums[i]
    return sum


# Tests
if __name__ == "__main__":
    print(sum13([1, 2, 2, 1]))
    print(sum13([1, 1]))
    print(sum13([1, 2, 2, 1, 13]))
    print(sum13([1, 2, 13, 2, 1, 13]))