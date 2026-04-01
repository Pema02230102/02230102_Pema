# ======================================
# QUEUE IMPLEMENTATION USING LINKED LIST
# ======================================

# Node class for linked list
class Node:
    def __init__(self, data):
        # Store element
        self.data = data
        # Pointer to next node
        self.next = None


class LinkedQueue:
    def __init__(self):
        # Front points to first node
        self._front = None

        # Rear points to last node
        self._rear = None

        # Size of queue
        self._size = 0

        print("Created new LinkedQueue")
        print("Queue is empty:", self.is_empty())

    def enqueue(self, element):
        # Create new node
        new_node = Node(element)

        # If queue is empty
        if self._rear is None:
            self._front = self._rear = new_node
        else:
            # Insert at rear
            self._rear.next = new_node
            self._rear = new_node

        self._size += 1
        print(f"Enqueued {element} to the queue")

    def dequeue(self):
        # Check if empty
        if self.is_empty():
            print("Queue Underflow!")
            return

        # Remove front node
        temp = self._front
        self._front = self._front.next

        # If queue becomes empty
        if self._front is None:
            self._rear = None

        self._size -= 1

        print(f"Dequeued element: {temp.data}")
        return temp.data

    def peek(self):
        # Return front element
        if self.is_empty():
            return None
        return self._front.data

    def is_empty(self):
        return self._front is None

    def size(self):
        return self._size

    def display_list(self):
        # Display in list format: [10,20,30]
        if self.is_empty():
            print("Display queue:[]")
            return

        elements = []
        current = self._front

        while current:
            elements.append(current.data)
            current = current.next

        # Print without spaces after commas (to match lab)
        print("Display queue:[" + ",".join(map(str, elements)) + "]")

    def display_linked(self):
        # Display in linked format: 20 -> 30 -> null
        if self.is_empty():
            print("Current queue: null")
            return

        current = self._front
        result = ""

        while current:
            result += str(current.data) + " -> "
            current = current.next

        result += "null"
        print("Current queue:", result)


# ==========================
# MAIN PROGRAM (TESTING)
# ==========================

lq = LinkedQueue()

lq.enqueue(10)
lq.display_list()

lq.enqueue(20)
lq.display_list()

lq.enqueue(30)
lq.display_list()

print("Front element:", lq.peek())

lq.dequeue()

lq.display_linked()

print("Queue size:", lq.size())