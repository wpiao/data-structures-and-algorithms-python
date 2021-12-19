class Node():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList():
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            else:
                current = current.next
        return False

    def to_string(self):
        current = self.head
        result = ""
        while current:
            result += "{ " + str(current.value) + " } -> "
            current = current.next
        return result + "None"
