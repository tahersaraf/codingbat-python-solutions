"""
CodingBat: count_evens
https://codingbat.com/prob/p189616

Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.
"""

def count_evens(nums):
    return len([num for num in nums if num%2==0])

# Tests
if __name__ == "__main__":
    print(count_evens([2, 1, 2, 3, 4]))
    print(count_evens([2, 2, 0]))
    print(count_evens([1, 3, 5]))