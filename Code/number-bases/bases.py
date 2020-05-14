#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace

dig_list = string.digits + string.ascii_lowercase
def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    power = 0
    value = []
    for char in digits:
        num = dig_list.find(char)
        value = [num] + value
    output = 0
    for char in value:
        a = int(char) * (base**power) 
        output = a + output 
        power += 1 
    return output


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    output = []
    while number != 0:
        wn = int(number/base)
        r = number % base 
        wn, r = divmod(number, base)
        c = dig_list[r]
        output = [c] + output
        number = wn
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    output = (''.join(output))
    print(output)
    return output



def convert(digits, base2, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # TODO: Convert digits from base 2 to base 16 (and vice versa)
    # ...
    enin = decode(digits, base1)
    # ...
    return encode(enin, base2)
print(convert('31', 10, 16))
     
# create function with n, 
# while n! = n*(n-1) == 0
# return value 





def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')
        

if __name__ == '__main__':
    main()



lst = [2, 3, 5, 6, 7]
target = 5
def recur(lst, index, target):
    a = lst[index]
    if a == target:
        return True
    elif index == len(lst) - 1:
        return False
    else:
        return recur(lst, index+1, target)
