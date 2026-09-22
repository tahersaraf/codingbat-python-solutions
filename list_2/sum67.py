"""
CodingBat: sum67
https://codingbat.com/prob/p108886

Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.
"""

def sum67(nums):
    sum = 0
    skip = False
    for i in range(len(nums)):
        if skip:
            if nums[i] == 7:
                skip = False
            continue
        if nums[i] == 6:
            skip = True
            continue

        sum += nums[i]
    return sum


# Tests
if __name__ == "__main__":
    print(sum67([1, 2, 2]))
    print(sum67([1, 2, 2, 6, 99, 99, 7]))
    print(sum67([1, 1, 6, 7, 2]))