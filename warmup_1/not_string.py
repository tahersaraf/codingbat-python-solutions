"""
CodingBat: not_string
https://codingbat.com/prob/p189441

Given a string, return a new string where "not " has been added to the front. 
However, if the string already begins with "not", return the string unchanged.
"""

def not_string(str):
    if not str.startswith('not'):
        return 'not ' + str
    else:
        return str

# Tests
if __name__ == "__main__":
    print(not_string('candy'))  # 'not candy'
    print(not_string('x'))      # 'not x'
    print(not_string('not bad'))# 'not bad'
    print(not_string('bad'))    # 'not bad'
    print(not_string('not'))    # 'not'
    print(not_string('is not')) # 'not is not'