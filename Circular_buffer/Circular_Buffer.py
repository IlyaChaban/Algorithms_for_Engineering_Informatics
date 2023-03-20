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

        self.start_node = Node(None, None, None)
        self.wr_ptr = self.start_node
        self.read_ptr = self.start_node
        self.read_flag = False
        self.elements_in_buffer = 0

        temp_last_node = self.start_node
        for i in range(size-1):
            new_empty_node = Node(None, None, None)
            if i != size-2:
                temp_last_node.next = new_empty_node
                new_empty_node.previous = temp_last_node
                temp_last_node = new_empty_node
            else:
                new_empty_node.next = self.start_node
                new_empty_node.previous = temp_last_node

                temp_last_node.next = new_empty_node
                self.start_node.previous = new_empty_node


    def read_from_buffer(self):
        if self.read_ptr != self.wr_ptr and self.read_flag == False:
            print(self.read_ptr.value)
            self.read_ptr = self.read_ptr.next
        elif self.read_ptr != self.wr_ptr and self.read_flag == True:
            self.read_ptr = self.read_ptr.next
            print(self.read_ptr.value)
        elif self.read_ptr == self.wr_ptr:
            print(self.read_ptr.value, "this was last value in buffer you can't read anymore")
            self.read_flag = True

    def write_to_buffer(self, value: str):
        new_Node = Node(None, None, value)
        if self.start_node.value == None:
            print(f"adding first  Node with value of: {value}")
            new_Node.next = self.start_node.next
            new_Node.previous = self.start_node.previous
            self.start_node.previous.next = new_Node
            self.start_node.next.previous = new_Node
            self.start_node = new_Node
            self.wr_ptr = new_Node
            self.read_ptr = new_Node

        elif self.wr_ptr.next != self.read_ptr:
            print(f"adding middle Node with value of: {value}")
            new_Node.previous = self.wr_ptr
            new_Node.next = self.wr_ptr.next.next

            self.wr_ptr.next.next.previous = new_Node
            self.wr_ptr.next = new_Node

            self.wr_ptr = new_Node

        elif self.wr_ptr.next == self.read_ptr:
            print("Buffer is full")



if __name__ == "__main__":
    buff = circularBuffer(5)

    temp_node = buff.start_node
    for i in range(5):
        print(temp_node.value)
        temp_node = temp_node.next

    for i in range(10):
        buff.write_to_buffer(f"{i}")

    for _ in range(10):
        buff.read_from_buffer()

    buff.write_to_buffer("5")
    buff.write_to_buffer("6")
    buff.read_from_buffer()
    buff.write_to_buffer("7")
    buff.read_from_buffer()
    buff.write_to_buffer("8")
    buff.read_from_buffer()
    buff.read_from_buffer()
    buff.read_from_buffer()
    buff.write_to_buffer("9")
    buff.read_from_buffer()

