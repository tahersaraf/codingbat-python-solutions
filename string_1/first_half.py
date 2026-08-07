"""
CodingBat: first_half
https://codingbat.com/prob/p107010

Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".

"""

def first_half(str):
    end = len(str)//2
    return str[:end]

# Tests
if __name__ == "__main__":
    print( first_half('WooHoo') )
    print( first_half('HelloThere') )
    print( first_half('abcdef') )