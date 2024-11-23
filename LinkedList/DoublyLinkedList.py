
class Node:
    def __init__(self,data,prev=None,next=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return f'{self.data} --> {self.next}'
            
    def __repr__(self):
        return f'{self.data} --> {self.next}'


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0


    def insert_at_beginnig(self, data):
        new = Node(data,None, None)
        if self.head is None:
            self.head = new
            return
        new.next = self.head
        self.head.prev = new
        self.head = new


    def show(self):
        curr = self.head
        result = ''
        while curr:
            result += str(curr.data) + " --> "
            curr = curr.next
        result += "None"
        print(result)
    
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        curr = self.head
        while curr:
            if not curr.next:
                break
            curr = curr.next
        newEnd = Node(data, prev=curr)
        curr.next = newEnd

dll = DoublyLinkedList()
dll.insert_at_end(1)
dll.insert_at_end(2)
dll.insert_at_end(3)
dll.insert_at_beginnig(4)
dll.show()