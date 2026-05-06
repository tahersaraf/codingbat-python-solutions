"""
CodingBat: front_back
https://codingbat.com/prob/p153599

Given a string, return a new string where the first and last chars have been exchanged.
"""

def front_back(str):
    n = len(str)
    if n > 1:
        return str[n-1] + str[1:n-1] + str[0]
    else:
        return str

# Tests
if __name__ == "__main__":
    print(front_back('code'))  # 'eodc'
    print(front_back('a'))     # 'a'
    print(front_back('ab'))    # 'ba'
    print(front_back('abc'))   # 'cba'
    print(front_back(''))      # ''