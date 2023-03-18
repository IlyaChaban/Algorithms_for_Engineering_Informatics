"""
This file is an implementation of Circular Buffer
"""

class Node:
    """
    implements node for circular buffer
    """
    def __init__(self, next, previous, value:str) -> None:
        self.value = value
        self.next = next
        self.previous = previous

class circularBuffer:
    """
    implementation of circular buffer
    """
    def __init__(self, size):
        self.size = size
        self.elements_in_buffer = 0
        self.start_node = None
        # Empty circular buffer initialization
        for i in range(self.size):
            next_node = Node(None, None, "")
            if i == 0:
                start_node = next_node
                last_node = next_node
            elif 0 < i <= self.size-1:
                last_node.next = next_node
                next_node.previous = last_node
                last_node = next_node
            elif i == self.size:
                last_node.next = start_node
                start_node.previous = last_node

        self.start_node = start_node
        self.read = start_node
        self.write = start_node

    def read_from_buffer(self):
        if self.read.next == self.write:
            print("there is no more elements to read")
        else:
            print(self.read.value)
            self.read = self.read.next

    def write_to_buffer(self, value: str):
        if self.elements_in_buffer == 0:
            self.write.value = value
            self.write = self.write.next
            self.elements_in_buffer = self.elements_in_buffer + 1

        elif self.write.next == self.read:
            print("you can't add more to the memory")

        elif self.write.next != self.read:
            self.write.value = value
            self.elements_in_buffer = self.elements_in_buffer + 1


if __name__ == "__main__":
    Buffer = circularBuffer(5)
    start_node = Buffer.start_node
    Buffer.write_to_buffer("1")

    for _ in range(10):
        Buffer.write_to_buffer("2")

    for i in range(5):
        print(start_node.value)
        start_node = start_node.next



