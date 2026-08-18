"""
CodingBat: sum3
https://codingbat.com/prob/p191645

Given an array of ints length 3, return the sum of all the elements.
"""

def sum3(nums):
    if len(nums) == 3:
        return nums[0]+nums[1]+nums[2]
    else:
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
        return sum

# Tests
if __name__ == "__main__":
    print(sum3([1, 2, 3]))
    print(sum3([5, 11, 2]))
    print(sum3([7, 0, 0]))
    print(sum3([7, 0, 0, 8, 1]))