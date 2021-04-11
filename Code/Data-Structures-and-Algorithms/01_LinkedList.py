class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.start = None

    def insert(self, value):
        if self.start == None:
            self.start = Node(value)

        current = self.start

        while current.next is not None:
            current = current.next

        current.next = Node(value)

linked_List = LinkedList()
linked_List.insert(1)
linked_List.insert(2)
linked_List.insert(3)
linked_List.insert(4)
linked_List.insert(5)