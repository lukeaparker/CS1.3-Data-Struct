#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return is_palindrome_recursive(text)

def is_palindrome_iterative(text):
    # TODO: implement the is_palindrome function iteratively here
    text_len = len(text)
    index_start = 0
    index_stop = text_len - 1

    while index_start <= index_stop:
        while text[index_start].isalnum() is False:
            index_start += 1

        #Decrement until alphabetic characters are hit
        while text[index_stop].isalnum() is False:
            index_stop -= 1

        if text[index_start].lower() != text[index_stop].lower():
            return False


        
        

        
        index_start +=1
        index_stop -= 1 
    return True

def is_palindrome_recursive(text, index_start=None, index_stop=None):
    text_length = len(text)
    if text_length < 2:
        return True
    if index_start == None:
        index_start = 0
    if index_stop == None:
        index_stop = text_length - 1

    if text[index_start].isalpha() != True:
        return is_palindrome_recursive(text, index_start+1, index_stop)
    if text[index_stop].isalpha() != True:
        return is_palindrome_recursive(text, index_start, index_stop-1)
    if index_start > index_stop:
        return True 
    if text[index_start].lower() != text[index_stop].lower():
        return False 
    else:
        return is_palindrome_recursive(text, index_start+1, index_stop-1)        




    





def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    # main()
    print(is_palindrome_iterative('no, on!'))