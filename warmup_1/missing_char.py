"""
CodingBat: missing_char
https://codingbat.com/prob/p149524


Given a non-empty string and an int n, return a new string where the char at index n has been removed. 
The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).
"""

def missing_char(str, n):
    start = str[:n]
    end = str[n+1:]
    return start + end

# Tests
if __name__ == "__main__":
    print(missing_char('kitten', 1))  # 'ktten'
    print(missing_char('kitten', 0))  # 'itten'
    print(missing_char('kitten', 4))  # 'kittn'
    print(missing_char('Hi', 0))      # 'i'
    print(missing_char('Hi', 1))      # 'H'
    print(missing_char('code', 0))    # 'ode'
    print(missing_char('code', 1))    # 'cde'
    print(missing_char('code', 2))    # 'coe'