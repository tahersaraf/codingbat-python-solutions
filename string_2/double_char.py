"""
CodingBat: double_char
https://codingbat.com/prob/p170842

Given a string, return a string where for every char in the original, there are two chars.
"""

def double_char(str):
    result = ""
    for s in str:
        result += s + s
    return result 

# Tests
if __name__ == "__main__":
    print(double_char('The'))
    print(double_char('AAbb'))
    print(double_char('Hi-There'))