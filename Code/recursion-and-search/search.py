#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    if index == len(array):
        return None
    if array[index] == item:
        return index
    else:
        index += 1 
        return linear_search_recursive(array, item, index)

def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    array.sort()
    low = 0
    high = len(array) - 1

    if array[0] == item:
        return 0
    elif array[high] == item:
        return high

    while low <= high:
        mid = (low + high) // 2

        # print((mid, low), (mid, high))
        if array[mid] == item:
            return mid 
        elif array[mid] < item:
            low = mid + 1
        else:
            high = mid -1
    return None



def binary_search_recursive(array, item, left=None, right=None):
    if left == None and right == None:
        left = 0
        right = len(array) - 1
        if array[0] == item:
            return 0
        elif array[right] == item:
            return right
    mid = (left + right) // 2 
    if right < left:
        return None

    if array[mid] == item:
        return mid
    if array[mid] < item:
        left = mid + 1
        return binary_search_recursive(array, item, left, right)
    elif item < array[mid]:
        right = mid - 1
        return binary_search_recursive(array, item, left, right)
