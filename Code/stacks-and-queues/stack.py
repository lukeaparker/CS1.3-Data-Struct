#!python
import sys
from linkedlist import LinkedList, Node


# Implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class LinkedStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        if self.length() == 0:
            return True 
        if self.length() != 0:
            return False

    def length(self):
        """Return the number of items in this stack."""
        return self.list.length()


    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(1) – reassigns next refrence"""
        # TODO: Push given item
        self.list.prepend(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        if self.is_empty():
            return None
        return self.list.head.data

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(1) – deletes and reassigns next refrence"""
        if self.is_empty() == True:
            raise ValueError
        else:
            node = self.list.head.data
        self.list.delete(node)
        return node



# def test_stack():
#     stack = LinkedStack()
#     stack.push('a')
#     stack.push('s')
#     print(stack.is_empty())
#     print(stack.peek())
#     stack.pop()
#     print(stack)
#     print(stack.peek())
    



# Implement ArrayStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class ArrayStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        if len(self.list) == 0:
            return True 
        else:
            return False
        

    def length(self):
        """Return the number of items in this stack."""
        if self.is_empty() == True:
            return 0
        else:
            return len(self.list) 

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(1) – appends to end of list"""
        return self.list.append(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        if self.is_empty():
            return None

        top = self.list[self.length() - 1]
        return top



    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(n) – has to shift indicies"""
        if self.is_empty() == True:
            raise ValueError('Stack is empty')
        else:
            return self.list.pop()

    
# Implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
#     stack = ArrayStack()
#     stack.push('a')
#     stack.push('b')
#     stack.push('d')
#     print(stack.length())
#     print(stack.is_empty())
#     stack.pop()
#     print(stack.peek())
# test_stack()

Stack = LinkedStack    
