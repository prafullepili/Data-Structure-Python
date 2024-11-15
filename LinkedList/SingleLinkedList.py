class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def insert_at_beginig(self, data):
        node = Node(data, self.head)
        self.length += 1
        self.head = node

    def print(self):
        if self.head is None:
            return
        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data) + " --> "
            itr = itr.next
        llstr += "None"
        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data)
            self.length += 1
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        self.length += 1
        itr.next = Node(data)

    def list_to_linkedList(self, data_list):
        """list[] of dat_lista \nEx: [12,4,3]"""
        self.head = None
        self.length = 0
        for data in data_list:
            self.insert_at_end(data)

    def remove_at(self, index):
        if index < 0 or index >= self.length:
            raise Exception("Invalid index")

        if index == 0:
            deleted = self.head
            self.head = self.head.next
            self.length -= 1
            return f"{deleted.data}"

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                self.length -= 1
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index > self.length:
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_beginig(data)
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                self.length += 1
                itr.next = Node(data, itr.next)
                break
            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)
            self.length += 1
            return
        itr = self.head
        while itr:
            if itr.data == data_after:
                break
            itr = itr.next
        if itr:
            itr.next = Node(data_to_insert, itr.next)
            self.length += 1
        else:
            raise Exception(f"{data_after} not in List")

    def remove_by_value(self, data):
        if self.head.data == data:
            self.head = self.head.next
            self.length -= 1
            return
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                self.length -= 1
                break
            itr = itr.next
