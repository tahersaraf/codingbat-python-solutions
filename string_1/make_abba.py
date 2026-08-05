"""
CodingBat: make_abba
https://codingbat.com/prob/p182144

Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".
"""

def make_abba(a, b):
    return a+b+b+a

# Tests
if __name__ == "__main__":
    print(make_abba('Hi', 'Bye'))
    print(make_abba('Yo', 'Alice'))
    print(make_abba('What', 'Up'))