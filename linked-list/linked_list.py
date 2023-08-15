class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
            
    
    def prepend(self, value):
        if self.length == 0:
            self.append(value)
        else:
            new_node = Node(value, self.head)
            self.head = new_node
            self.length += 1
            
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        if self.length == 1:
            self.tail = None
        self.length -= 1
        
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
        
    def insert(self, index, value):
        pass
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            if temp.value is not None:
                print(temp.value)
            temp = temp.next