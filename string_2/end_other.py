"""
CodingBat: end_other
https://codingbat.com/prob/p174314

Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.
"""

# def end_other(a, b):
    # if min(len(a),len(b)) == len(a):
    #     s = a.lower()
    #     str = b.lower()
    # else:
    #     s = b.lower()
    #     str = a.lower()

    # for i in range(len(str)-1):
    #     return str[len(str)-len(s):] == s

def end_other(a, b):
  a = a.lower()
  b = b.lower()
  return (b.endswith(a) or a.endswith(b))
        

# Tests
if __name__ == "__main__":
    print(end_other('Hiabc', 'abc'))
    print(end_other('AbC', 'HiaBc'))
    print(end_other('abc', 'abXabc'))