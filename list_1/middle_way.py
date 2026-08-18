"""
CodingBat: middle_way
https://codingbat.com/prob/p171011

Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements..
"""

def middle_way(a, b):
    mid_a = a[len(a)//2]
    mid_b = b[len(b)//2]
    return [mid_a,mid_b]

# Tests
if __name__ == "__main__":
    print(middle_way([1, 2, 3], [4, 5, 6]))
    print(middle_way([7, 7, 7], [3, 8, 0]))
    print(middle_way([5, 2, 9], [1, 4, 5]))