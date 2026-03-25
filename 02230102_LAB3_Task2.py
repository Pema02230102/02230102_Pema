# ======================================
# STACK IMPLEMENTATION USING LINKED LIST
# ======================================

# Node class represents each element in the stack
class Node:
    def __init__(self, data):
        # Store value of node
        self.data = data

        # Pointer to next node
        self.next = None


class LinkedStack:
    def __init__(self):
        # Top points to the first node of stack
        self.top = None

        # Variable to track number of elements
        self._size = 0

        # Initial output (must match instruction)
        print("Created new LinkedStack")
        print("Stack is empty:", self.is_empty())

    def push(self, element):
        # Create new node
        new_node = Node(element)

        # Link new node to current top
        new_node.next = self.top

        # Update top to new node
        self.top = new_node

        # Increase size
        self._size += 1

        print(f"Pushed {element} to the stack")

    def pop(self):
        # Check if stack is empty
        if self.is_empty():
            print("Stack Underflow!")
            return

        # Store value of top node
        popped = self.top.data

        # Move top pointer to next node
        self.top = self.top.next

        # Decrease size
        self._size -= 1

        print(f"Popped element: {popped}")

        return popped

    def peek(self):
        # Return top element without removing
        if self.is_empty():
            return None
        return self.top.data

    def is_empty(self):
        # Stack is empty if top is None
        return self.top is None

    def size(self):
        # Return total number of elements
        return self._size

    def display_push_format(self):
        """
        This function prints stack in LIST FORMAT
        Example: [30,20,10]
        Used AFTER PUSH operations (as per instruction)
        """
        if self.is_empty():
            print("Display stack: []")
            return

        current = self.top
        elements = []

        # Traverse and store elements
        while current:
            elements.append(current.data)
            current = current.next

        # Print in required format
        print("Display stack:", elements)

    def display_pop_format(self):
        """
        This function prints stack in LINKED FORMAT
        Example: 20 -> 10 -> null
        Used AFTER POP operation (as per instruction)
        """
        if self.is_empty():
            print("Current stack: null")
            return

        current = self.top

        print("Current stack:", end=" ")

        # Traverse linked list
        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("null")


# =============
# MAIN PROGRAM 
# =============
stack = LinkedStack()

# Push operations
stack.push(10)
stack.display_push_format()

stack.push(20)
stack.display_push_format()

stack.push(30)
stack.display_push_format()

# Peek
print("Top element:", stack.peek())

# Pop
stack.pop()

# Display in linked format (IMPORTANT difference)
stack.display_pop_format()

# Size
print("Stack size:", stack.size())