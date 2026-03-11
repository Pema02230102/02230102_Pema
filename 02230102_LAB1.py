# Create a class called CustomList
class CustomList:

    # Constructor to initialize array with default capacity 10
    def __init__(self):
        self.data = [None] * 10   # array to store elements
        self.capacity = 10       # maximum capacity
        self.current_size = 0    # current number of elements
        print("Created new CustomList with capacity:", self.capacity)
        print("Current size:", self.current_size)

    # Add element to the end
    def append(self, element):
        self.data[self.current_size] = element
        self.current_size += 1
        print("Appended", element, "to the list")

    # Get element at a specific index
    def get(self, index):
        return self.data[index]

    # Replace element at a specific index
    def set(self, index, element):
        self.data[index] = element
        print("Set element at index", index, "to", element)

    # Return current size
    def size(self):
        return self.current_size


# Example usage
cl = CustomList()

cl.append(5)
print("Element at index 0:", cl.get(0))

cl.set(0, 10)
print("Element at index 0:", cl.get(0))

print("Current size:", cl.size())