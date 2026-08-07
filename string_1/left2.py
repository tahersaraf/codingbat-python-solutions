"""
CodingBat: left2
https://codingbat.com/prob/p160545

Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will be at least 2.
"""

def left2(str):
    return str[2:] + str[:2]


# Tests
if __name__ == "__main__":
    print( left2('Hello') )
    print( left2('java') )
    print( left2('Hi') )