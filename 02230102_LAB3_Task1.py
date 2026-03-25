# ================================
# STACK IMPLEMENTATION USING ARRAY
# ================================

class ArrayStack:
    def __init__(self, capacity=10):
        # Create a fixed-size list (array) to store stack elements
        # Initially, all positions are None
        self._data = [None] * capacity

        # The top variable keeps track of the index of the last inserted element
        # -1 means the stack is currently empty
        self._top = -1

        # Store maximum capacity of the stack
        self._capacity = capacity

        # Display initial messages as required in lab output
        print(f"Created new ArrayStack with capacity: {capacity}")
        print("Stack is empty:", self.is_empty())

    def push(self, element):
        # Before inserting, check if stack is full
        if self._top == self._capacity - 1:
            print("Stack Overflow!")   # Cannot insert more elements
            return

        # Move top pointer to next position
        self._top += 1

        # Insert the new element at the top position
        self._data[self._top] = element

        # Display message (as per expected output)
        print(f"Pushed {element} to the stack")

    def pop(self):
        # Check if stack is empty before removing element
        if self.is_empty():
            print("Stack Underflow!")  # Nothing to remove
            return

        # Get the top element
        element = self._data[self._top]

        # Reduce the top pointer (removing the element logically)
        self._top -= 1

        # Display removed element
        print(f"Popped element: {element}")

        return element

    def peek(self):
        # Return the top element WITHOUT removing it
        if self.is_empty():
            return None
        return self._data[self._top]

    def is_empty(self):
        # Stack is empty if top pointer is -1
        return self._top == -1

    def size(self):
        # Number of elements = top index + 1
        return self._top + 1

    def display(self):
        # Display elements from bottom to top
        if self.is_empty():
            print("Display stack: []")
        else:
            # Slice the array up to top index
            print("Display stack:", self._data[:self._top + 1])


# ==========================
# MAIN PROGRAM (TESTING)
# ==========================

# Create a stack object
stack = ArrayStack()

# Push elements one by one
stack.push(10)
stack.display()

stack.push(20)
stack.display()

stack.push(30)
stack.display()

# Show top element without removing
print("Top element:", stack.peek())

# Remove top element
stack.pop()

# Show current size
print("Stack size:", stack.size())

# Final display
stack.display()