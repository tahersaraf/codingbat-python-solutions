"""
CodingBat: hello_name
https://codingbat.com/prob/p115413

Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".
"""

def hello_name(name):
    return "Hello " +name+"!"

# Tests
if __name__ == "__main__":
    print(hello_name('Bob'))
    print(hello_name('Alice'))
    print(hello_name('X'))