class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
        last = self.head
        while last.next != self.head:
            last = last.next
        last.next = new_node
        new_node.next = self.head

    def delete_node(self, key):
        if self.head is None:
            return
        last = self.head
        if self.head.data == key:
            while last.next != self.head:
                last = last.next
            if self.head == self.head.next:
                self.head = None
            else:
                last.next = self.head.next
                self.head = last.next
            return
        prev = None
        temp = self.head
        while temp.next != self.head:
            if temp.data == key:
                prev.next = temp.next
                return
            prev = temp
            temp = temp.next

    def print_list(self):
        current = self.head
        if self.head is not None:
            while True:
                print(current.data, end=" ")
                current = current.next
                if current == self.head:
                    break

cll = CircularLinkedList()
cll.insert_at_end(1)
cll.insert_at_end(2)
cll.insert_at_end(3)
cll.delete_node(2)
cll.print_list()
