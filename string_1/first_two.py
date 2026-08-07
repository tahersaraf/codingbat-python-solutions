"""
CodingBat: first_two
https://codingbat.com/prob/p184816

Given a string, return the string made of its first two chars, so the String "Hello" yields "He". If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" yields the empty string "".
"""

def first_two(str):
    if len(str) > 2:
        return str[:2]
    return str

# Tests
if __name__ == "__main__":
    print( first_two('Hello') )
    print( first_two('abcdefg') )
    print( first_two('ab') )