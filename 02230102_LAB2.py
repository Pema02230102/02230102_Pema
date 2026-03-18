# Linked List Implementation (LAB 2)

# Node class → represents each element in the list
class Node:
    def __init__(self, data):
        self.data = data      # store value
        self.next = None      # pointer to next node


# LinkedList class → manages all nodes
class LinkedList:
    def __init__(self):
        self.head = None      # first node
        self.size = 0         # number of elements
        
        # initial output
        print("Created new LinkedList")
        print("Current size:", self.size)
        print("Head:", self.head)

    # Append → add element at end
    def append(self, data):
        new = Node(data)      # create new node
        
        if self.head is None:     # if list is empty
            self.head = new
        else:
            temp = self.head
            while temp.next:      # move to last node
                temp = temp.next
            temp.next = new       # connect new node at end
        
        self.size += 1
        print(f"Appended {data} to the list")

    # Prepend → add element at beginning
    def prepend(self, data):
        new = Node(data)
        new.next = self.head  # new node points to old head
        self.head = new       # update head
        
        self.size += 1
        print(f"Prepend {data} to the list")

    # Get → display element at given index
    def get(self, index):
        if index < 0 or index >= self.size:
            print("Index out of range")
            return
        
        temp = self.head
        for _ in range(index):    # move to required position
            temp = temp.next
        
        print(f"Element at index {index}: {temp.data}")

    # Set → update element at given index
    def set(self, index, data):
        if index < 0 or index >= self.size:
            print("Index out of range")
            return
        
        temp = self.head
        for _ in range(index):    # move to required position
            temp = temp.next
        
        temp.data = data
        print(f"Set element at index {index} to {data}")

    # Print → display full list
    def print_list(self):
        temp = self.head
        print("Print Linked list :[", end="")
        
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        
        print("]")


# -------- Testing --------

l = LinkedList()

l.append(5)       # list: 5
l.get(0)

l.set(0, 10)      # list: 10
l.get(0)

print("Current size:", l.size)

l.prepend(10)     # list: 10 10

l.print_list()