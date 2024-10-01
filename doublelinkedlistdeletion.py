class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def delete_node(self, key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                if self.head:
                    self.head.prev = None
                temp = None
                return
        while temp is not None:
            if temp.data == key:
                break
            temp = temp.next
        if temp is None:
            return
        if temp.next is not None:
            temp.next.prev = temp.prev
        if temp.prev is not None:
            temp.prev.next = temp.next
        temp = None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next

dll = DoublyLinkedList()
dll.insert_at_end(1)
dll.insert_at_end(2)
dll.insert_at_end(3)
dll.delete_node(2)
dll.print_list()
