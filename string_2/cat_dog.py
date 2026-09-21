"""
CodingBat: cat_dog
https://codingbat.com/prob/p164876

Return True if the string "cat" and "dog" appear the same number of times in the given string.
"""

def cat_dog(str):
    count_cat = 0
    count_dog = 0
    for i in range(len(str)-1):
        if str[i:i+3] == 'cat':
            count_cat += 1
        if str[i:i+3] == 'dog':
            count_dog += 1

    return count_dog == count_cat

# Tests
if __name__ == "__main__":
    print(cat_dog('catdog'))
    print(cat_dog('catcat'))
    print(cat_dog('1cat1cadodog'))