from solved.array_stack import Empty


class LinkedStack:
    """LIFO Stack implementation using a singly linked list for storage"""

    class _Node:
        """Lightweight nonpublic class for storing a singly linked node"""
        __slots__ = '_element', '_next'  # streamline memory usage

        def __init__(self, element, next):  # initialize node's fields
            self._element = element  # reference to user's element
            self._next = next  # reference to next node

    def __init__(self):
        """Create an empty stack."""
        self._head = None
        self._size = 0

    def __len__(self):
        """Return the number of elements in the stack."""
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        """Add element e to the top of the stack."""
        self._head = self._Node(e, self._head)
        self._size += 1

    def top(self):
        """Return but donot remove the element at the top of the stack.
        Raise Empty exception if the stack is empty"""
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element

    def pop(self):
        """Remove and return the element from the top of the stack
        Raise Empty exception if the stack is empty"""

        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size = 1
        return answer
