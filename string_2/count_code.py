"""
CodingBat: count_code
https://codingbat.com/prob/p186048

Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.
"""

def count_code(str):
    count = 0
    for i in range(len(str)-1):
        if str[i:i+4].startswith('co') and str[i:i+4].endswith('e'):
            count +=1
    return count


# Tests
if __name__ == "__main__":
    print(count_code('aaacodebbb'))
    print(count_code('codexxcode'))
    print(count_code('cozexxcope'))