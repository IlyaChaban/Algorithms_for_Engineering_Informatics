"""
This file is an implementation of Circular Buffer
"""

class Node:
    """
    implements Node for circular buffer
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
        """
        init function creates empty circular buffer and necessary variable to work with it
        :param size: describes size of circular buffer
        :param start_node: defines start node for initialization
        :param read_ptr: defines read pointer
        :param wr_ptr: defines write pointer
        :param read_flag: defines order in which i will read values and move pointer True - move->read; False - opposite
        """
        self.size = size

        self.start_node = Node(None, None, None)
        self.wr_ptr = self.start_node
        self.read_ptr = self.start_node
        self.full = False
        self.empty = True
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
        """
        this function reads values from circular buffer
        """
        if self.read_ptr != self.read_ptr or not self.empty:

            self.elements_in_buffer -= 1
            self.full = False
            self.read_ptr = self.read_ptr.next
            if self.elements_in_buffer == 0:
                print("you have read last element from buffer which is ")
                self.empty = True
            return self.read_ptr.previous.value
        else:
            print("buffer is empty")


    def write_to_buffer(self, value: str):
        """
        this function adds new Nodes to circular buffer
        """

        if self.wr_ptr != self.read_ptr or not self.full:
            self.wr_ptr.value = value
            self.elements_in_buffer += 1
            self.empty = False
            self.wr_ptr = self.wr_ptr.next
            if self.elements_in_buffer == self.size:
                print("you are added last element in buffer")
                self.full = True
        else:
            print("buffer is full")





if __name__ == "__main__":
    print("Initializing buffer with 5 elements in it\n")
    buff = circularBuffer(5)

    print("adding 5 elements into buffer")
    for i in range(5):
        print(f"adding to buffer value: {i}")
        buff.write_to_buffer(i)

    print("\nlooking at the buffer")
    temp_node = buff.read_ptr
    for _ in range(5):
        print(temp_node.value)
        temp_node = temp_node.next

    print("\ntrying to add more to the buffer which is full")
    buff.write_to_buffer(5)

    print("\n reading data from buffer")
    for i in range(5):
        print(buff.read_from_buffer())

    print("\ntrying to read empty buffer")
    print(buff.read_from_buffer())
    
    