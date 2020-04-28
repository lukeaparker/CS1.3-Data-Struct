#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text.
    O(n*m) where n is the length of the pattern and m is the length of the text"""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    index_patern = find_index(text, pattern)
    if index_patern == None:
        return False
    else:
        return True
    

def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found.
    O(n*m) where n is the length of the pattern and m is the length of the text"""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)


    t_index = 0
    p_index = 0
    if pattern == "":
        return 0
    elif len(pattern) == 1:
        for i, char in enumerate(text):
            if char == pattern:
                return i 

        return None

    while t_index < len(text):
        if text[t_index] == pattern[p_index]:
            if p_index == len(pattern) - 1:
                return t_index - p_index
            p_index += 1
            t_index += 1
        elif text[t_index] != pattern[p_index]:
            if p_index != 0:
                t_index -= p_index - 1
                p_index = 0 
            else:
                t_index += 1 
    return None
            
def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found.
    O(1) if item is the first that is checked
    O(n*m) where n is the length of the pattern and m is the length of the text"""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    first_i = []
    if pattern == "":
        return [i for i in range(len(text)) ]
    elif len(pattern) == 1:
        return [i for i, char in enumerate(text) if char == pattern ]


    t_index = 0
    p_index = 0
    while t_index < len(text):
        print((t_index, p_index), (len(text), len(pattern)))
        if text[t_index] == pattern[p_index]:
            if p_index == len(pattern) - 1:
                first_i.append(t_index - p_index)
                t_index -= p_index - 1
                p_index = 0 
            p_index += 1
            t_index += 1
        elif text[t_index] != pattern[p_index]:
            if p_index != 0:
                t_index -= p_index - 1
                p_index = 0 
            else:
                t_index += 1 
    return first_i
        

def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
    # print(find_index("looper", "er"))