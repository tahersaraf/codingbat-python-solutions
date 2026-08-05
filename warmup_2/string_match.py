"""
CodingBat: string_match
https://codingbat.com/prob/p182414

Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.
"""

def string_match(a, b):
    count = 0
    n = min(len(a), len(b))
    for i in range(n-1):
        if a[i] + a[i+1] == b[i] + b[i+1]:
            count += 1
    return count

# Tests
if __name__ == "__main__":
    print(string_match('xxcaazz', 'xxbaaz'))
    print(string_match('abc', 'abc'))
    print(string_match('abc', 'axc'))