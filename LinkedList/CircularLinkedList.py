class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
    
    def __exit__(self, *args, **kwds):
        self.show()
    
    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head is None:
            new_node.next = new_node
            self.head = new_node
            self.length += 1
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head
        self.length += 1
    
    def insert_at_beginning(self,data):
        new_node = Node(data)
        if self.head is None:
            new_node.next = new_node
            self.head = new_node
            self.length += 1
            return
        curr = self.head
        while curr.next != self.head:
            curr = curr.next
        curr.next = new_node
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def show(self):
        if self.head is None:
            print('None')
            return
        curr = self.head
        res = 'start -> '
        while True:
            res += f"{curr.data} --> "
            curr = curr.next
            if curr == self.head:
                break
        print(res + f"start -> {curr.data} --> ...")


    def append(self, data, index = None):
        if index is None:
            self.insert_at_end(data)
        elif index == 0:
            self.insert_at_beginning(data)
        else:
            if index > self.length - 1 or index < 0:
                raise IndexError('list assignment index out of range')
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            new_node = Node(data)
            temp = curr.next
            curr.next = new_node
            new_node.next = temp
            self.length +=1 


cll = CircularLinkedList()
cll.append(1)
cll.append(0,0)
cll.append(3)
cll.append(4)
cll.append(2,2)
print(cll.length)
cll.append(20,4)
print(cll.length)
cll.show()