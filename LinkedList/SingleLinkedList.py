class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def insert_at_beginnig(self, data):
        node = Node(data, self.head)
        self.length += 1
        self.head = node

    def insert_at_end(self, data):
        curr = self.head
        if self.head is not None:
            while curr.next:
                curr = curr.next
            curr.next = Node(data)
            self.length += 1
            return
        self.head = Node(data)
        self.length += 1

    def insert_at(self, position, data):
        if position < 0 or position > self.length:
            raise Exception(f"Invalid position. position should in between 0 - {self.length}")

        if position == 0:
            self.insert_at_beginnig(data)
        count = 0
        curr = self.head
        while curr:
            if count == position - 1:
                self.length += 1
                curr.next = Node(data, curr.next)
                break
            curr = curr.next
            count += 1

    def remove_from_beginnig(self):
        if self.head is not None:
            self.head = self.head.next
            self.length -= 1
            return
        raise ValueError('Empty node can not be deleted.')

    def remove_from_end(self):
        if not self.head:
            raise ValueError('List is empty.')
        if not self.head.next:
            self.head = None
            self.length -= 1
            return 
        curr = self.head
        while curr.next and curr.next.next:
            curr = curr.next
        curr.next = None    
        self.length -= 1    

    def remove_at(self, index):
        if index < 0 or index >= self.length:
            raise Exception(f"Invalid index. Index should between 0 - {self.length}")

        print(f'after delete at index {index}'.ljust(30), end="-->  ")
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

    def remove_by_value(self, data):
        if self.head.data == data:
            print(f"After delete {data}".ljust(30), end="--> ")
            self.head = self.head.next
            self.length -= 1
            return
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                print(f"After delete {data}".ljust(30), end="--> ")
                itr.next = itr.next.next
                self.length -= 1
                break
            itr = itr.next

    def list_to_linkedList(self, data_list):
        """list[] of dat_lista \nEx: [12,4,3]"""
        self.head = None
        self.length = 0
        print(f'\nCreated new linked list from given list', data_list)
        for data in data_list:
            self.insert_at_end(data)

    def insert_after_value(self, find, insert_value):
        if self.head.data == find:
            print(f"After inserted {insert_value} after {find}".ljust(30), end="--> ")
            self.head.next = Node(insert_value, self.head.next)
            self.length += 1
            return
        itr = self.head
        print(f"After inserted {insert_value} after {find}".ljust(30), end="--> ")
        while itr:
            if itr.data == find:
                break
            itr = itr.next
        if itr:
            itr.next = Node(insert_value, itr.next)
            self.length += 1
        else:
            raise Exception(f"{find} not in List")

    def show(self):
        if self.head is None:
            print('None')
            return 
        curr = self.head
        llstr = ""
        while curr:
            llstr += str(curr.data) + " --> "
            curr = curr.next
        llstr += "None"
        print(llstr)

    def find(self, data):
        curr = self.head
        count = 0
        while curr:
            if curr.data == data:
                break
            curr = curr.next
            count += 1
        if curr is None:
            return None
        return curr
    
    def find_replace(self, data, new_data):
        search_result = self.find(data)
        if search_result:
            search_result.data = new_data
            return
        print(f'{data} not found')
        return

    def reverse(self):
        curr = self.head
        prev = None
        print('After reverse'.ljust(30), end="--> ")
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        self.head = prev

        

llist = SingleLinkedList()
llist.insert_at_beginnig(10)
llist.insert_at_end(20)
llist.insert_at_beginnig(30)
llist.insert_at_end('end')
llist.insert_at(0,'start')
llist.show()
llist.remove_from_beginnig()
print('after delete from beginning'.ljust(30), end="-->  ")
llist.show()
print('after delete from end'.ljust(30), end="-->  ")
llist.remove_from_end()
llist.show()
llist.remove_at(2)
llist.show()
print('Final Length : ',llist.length)
llist.list_to_linkedList([12,34,64,65,76])
llist.show()
llist.insert_after_value(12, 100)
llist.show()
llist.remove_by_value(100)
llist.show()
llist.find(65)
llist.find_replace(643,'hi')
llist.reverse()
llist.insert_at_beginnig('Name')
llist.insert_at_end('Prafull')
llist.show()
print('Final Length : ',llist.length)
