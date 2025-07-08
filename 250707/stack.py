class Stack:
    """A simple Stack implementation using a Python list."""

    def __init__(self):
        """Initializes an empty stack."""
        self._items = []

    def is_empty(self):
        """Returns True if the stack is empty, False otherwise."""
        return not self._items

    def push(self, item):
        """Adds an item to the top of the stack."""
        self._items.append(item)

    def pop(self):
        """
        Removes and returns the item at the top of the stack.
        Raises an IndexError if the stack is empty.
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        """
        Returns the item at the top of the stack without removing it.
        Raises an IndexError if the stack is empty.
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def size(self):
        """Returns the number of items in the stack."""
        return len(self._items)

    def __str__(self):
        """Returns a string representation of the stack."""
        return str(self._items)

if __name__ == "__main__":
    # Create a new stack
    s = Stack()

    # Check if it's empty
    print(f"Is stack empty? {s.is_empty()}")

    # Push some items
    print("Pushing 1, 2, 3")
    s.push(1)
    s.push(2)
    s.push(3)
    print(f"Stack: {s}")
    print(f"Stack size: {s.size()}")

    # Peek at the top item
    print(f"Peek: {s.peek()}")

    # Pop an item
    print(f"Popped: {s.pop()}")
    print(f"Stack after pop: {s}")

    # Check if it's empty again
    print(f"Is stack empty? {s.is_empty()}")

    # Pop remaining items
    print(f"Popped: {s.pop()}")
    print(f"Popped: {s.pop()}")

    # Check if it's empty
    print(f"Is stack empty? {s.is_empty()}")

    # Try to pop from an empty stack
    try:
        s.pop()
    except IndexError as e:
        print(f"Error: {e}")
