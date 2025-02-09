
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

    def insert_at_beginning(self, data):
        new = Node(data,None, None)
        if self.head is None:
            self.head = new
            self.length += 1
            return
        new.next = self.head
        self.head.prev = new
        self.head = new
        self.length += 1

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data)
            self.length += 1
            return
        curr = self.head
        while curr:
            if not curr.next:
                break
            curr = curr.next
        newEnd = Node(data, prev=curr)
        curr.next = newEnd
        self.length += 1

    def insert_at(self, position, data):
        if position > self.length or position < 0:
            raise ValueError('Invalid Index')
        if position == 0:
            new_node = Node(data,None,self.head)
            self.head.prev = new_node
            self.head = new_node
            self.length += 1
            return
        curr = self.head
        counter = 1
        while curr and counter < position-1:
            curr = curr.next
            counter += 1
        new_node = Node(data,curr,curr.next)
        curr.next.prev = new_node
        curr.next = new_node
        self.length += 1
        self.head = self.head

    def delete_from_beginning(self):
        if self.length == 0:
            raise Exception('Invalid Operation: Empty list cannot delete')
        if self.head.next is None:
            self.length -= 1
            self.head = None
            return
        self.head.next.prev = None
        self.head = self.head.next
        self.length -= 1
        return

    def delete_from_end(self):
        if self.head is None:
            raise Exception('Invalid Operation: Empty list cannot delete')
        if self.head.next is None:
            self.length -= 1
            self.head = None
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.prev.next = None
        curr.prev = None
        self.length -= 1

    def show(self):
        curr = self.head
        result = ''
        while curr:
            result += str(curr.data) + " --> "
            curr = curr.next
        result += "None"
        print(result)

    def get_last_node(self):
        if self.head is None:
            return None
        curr = self.head
        while curr.next:
            curr = curr.next
        return curr

    def traverse_backward(self, head):
        curr = head
        backward_result = ''
        while curr:
            backward_result += f' <-- {str(curr.data)}'
            curr = curr.prev
        backward_result =  'None' + backward_result
        print(backward_result)

    def show_bidirection(self):
        self.traverse_backward(self.get_last_node())
        print(end="\t ")
        self.show()
    
    def delete(self,index):
        if index > self.length-1 or index < -1:
            raise IndexError('Invalid index')
        if self.length == 0:
            raise Exception('Invalid Operation: Empty list cannot delete')
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
            return
        curr = self.head    
        for _ in range(index-1):
            curr = curr.next
        curr.next = curr.next.next
        if curr.next is None:
            return
        curr.next.prev = curr
        self.length -= 1

dll = DoublyLinkedList()
dll.insert_at_end(1)
dll.insert_at_end(2)
dll.insert_at_end(3)
dll.insert_at_end(4)
dll.insert_at_beginning(0)
dll.insert_at(5,'last')
dll.insert_at_beginning('first')
dll.delete_from_end()
dll.show_bidirection()