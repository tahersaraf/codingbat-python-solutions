"""
CodingBat: centered_average
https://codingbat.com/prob/p126968

Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the array is length 3 or more.
"""

def centered_average(nums):
    nums.remove(max(nums))
    nums.remove(min(nums))

    return sum(nums)//len(nums)

# Tests
if __name__ == "__main__":
    print(centered_average([1, 2, 3, 4, 100]))
    print(centered_average([1, 1, 5, 5, 10, 8, 7]))
    print(centered_average([-10, -4, -2, -4, -2, 0]))