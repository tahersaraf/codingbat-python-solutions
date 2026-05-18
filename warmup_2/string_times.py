"""
CodingBat: string_times
https://codingbat.com/prob/p189441

Given a string and a non-negative int n, return a larger string that is n copies of the original string.
"""

def string_times(str, n):
    return str * n;

# Tests
if __name__ == "__main__":
    print(string_times("Hi",3))
    print(string_times("Yo",4))
