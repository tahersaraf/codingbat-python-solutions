"""
CodingBat: count_hi
https://codingbat.com/prob/p167246

Return the number of times that the string "hi" appears anywhere in the given string.
"""

def count_hi(str):
    count = 0
    for i in range(len(str)-1):
        if str[i]+str[i+1] == 'hi':
            count += 1
    return count

# Tests
if __name__ == "__main__":
    print(count_hi('abc hi ho'))
    print(count_hi('ABChi hi'))
    print(count_hi('hihi'))