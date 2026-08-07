"""
CodingBat: non_start
https://codingbat.com/prob/p127703

Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.
"""

def non_start(a, b):
  return a[1:] + b[1:]



# Tests
if __name__ == "__main__":
    print( non_start('Hello', 'There') )
    print(non_start('java', 'code') )
    print( non_start('shotl', 'java')  )