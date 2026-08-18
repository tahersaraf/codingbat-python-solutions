"""
CodingBat: max_end3
https://codingbat.com/prob/p135290


Given an array of ints length 3, figure out which is larger, the first or last element in the array, and set all the other elements to be that value. Return the changed array.
"""

def max_end3(nums):
    for i in range(len(nums)):
        nums[i] = max(nums[0],nums[2])
    return nums

# Tests
if __name__ == "__main__":
    print(max_end3([1, 2, 3]))
    print(max_end3([11, 5, 9]))
    print(max_end3([2, 11, 3]))