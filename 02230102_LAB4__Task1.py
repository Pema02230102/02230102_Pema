# =================================
# QUEUE IMPLEMENTATION USING ARRAY
# =================================

class ArrayQueue:
    def __init__(self, capacity=10):
        # Create a fixed-size list (array) to store queue elements
        self._data = [None] * capacity

        # Front points to the first element
        self._front = 0

        # Rear points to the last inserted element
        self._rear = -1

        # Number of elements in queue
        self._size = 0

        # Maximum capacity
        self._capacity = capacity

        # Initial messages (as per lab)
        print(f"Created new Queue with capacity: {capacity}")
        print("Queue is empty:", self.is_empty())

    def enqueue(self, element):
        # Check if queue is full
        if self._size == self._capacity:
            print("Queue Overflow!")
            return

        # Move rear in circular manner
        self._rear = (self._rear + 1) % self._capacity

        # Insert element
        self._data[self._rear] = element
        self._size += 1

        print(f"Enqueued {element} to the queue")

    def dequeue(self):
        # Check if queue is empty
        if self.is_empty():
            print("Queue Underflow!")
            return

        # Get front element
        element = self._data[self._front]

        # Move front forward
        self._front = (self._front + 1) % self._capacity
        self._size -= 1

        print(f"Dequeued element: {element}")
        return element

    def peek(self):
        # Return front element without removing
        if self.is_empty():
            return None
        return self._data[self._front]

    def is_empty(self):
        # Queue is empty if size is 0
        return self._size == 0

    def size(self):
        # Return number of elements
        return self._size

    def display(self):
        # Display queue elements from front to rear
        if self.is_empty():
            print("Display queue: []")
            return

        result = []
        index = self._front

        # Traverse queue circularly
        for _ in range(self._size):
            result.append(self._data[index])
            index = (index + 1) % self._capacity

        print("Display queue:", result)


# ==========================
# MAIN PROGRAM (TESTING)
# ==========================

queue = ArrayQueue()

queue.enqueue(10)
queue.display()

queue.enqueue(20)
queue.display()

queue.enqueue(30)
queue.display()

print("Front element:", queue.peek())

queue.dequeue()

queue.display()

print("Queue size:", queue.size())