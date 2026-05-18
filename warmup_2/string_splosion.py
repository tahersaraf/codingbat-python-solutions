"""
CodingBat: string_splosion
https://codingbat.com/prob/p118366


Given a non-empty string like "Code" 
return a string like "CCoCodCode".
"""

def string_splosion(str):
    result=""
    for i in range(len(str)):
        result += str[:i+1]
    return result

# Tests
if __name__ == "__main__":
    print(string_splosion('Code'))
    print(string_splosion('abc'))
    print(string_splosion('ab'))