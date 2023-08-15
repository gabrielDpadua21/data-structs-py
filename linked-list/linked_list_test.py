import unittest
import linked_list


class TestLinkedList(unittest.TestCase):
    
    def test_append(self):
        my_linked_list = linked_list.LinkedList(4)
        my_linked_list.append(5)
        my_linked_list.append(6)
        my_linked_list.append(7)
        self.assertEqual(my_linked_list.length, 4)
        
    def test_pop(self):
        my_linked_list = linked_list.LinkedList(4)
        my_linked_list.append(5)
        my_linked_list.append(6)
        my_linked_list.append(7)
        my_linked_list.pop()
        self.assertEqual(my_linked_list.length, 3)
        
    def test_pop_empty_list(self):
        my_linked_list = linked_list.LinkedList(4)
        my_linked_list.pop()
        self.assertEqual(my_linked_list.length, 0)
        
    def test_prepend(self):
        my_linked_list = linked_list.LinkedList(4)
        my_linked_list.prepend(5)
        self.assertEqual(my_linked_list.head.value, 5)
        
    def test_prepend_empty_list(self):
        my_linked_list = linked_list.LinkedList(4)
        my_linked_list.pop()
        my_linked_list.prepend(5)
        self.assertEqual(my_linked_list.head.value, 5)
        
    def test_pop_first(self):
        my_linked_list = linked_list.LinkedList(4)
        my_linked_list.append(5)
        my_linked_list.append(6)
        my_linked_list.append(7)
        my_linked_list.pop_first()
        self.assertEqual(my_linked_list.head.value, 5)
        
    def test_pop_first_empty_list(self):
        my_linked_list = linked_list.LinkedList(4)
        my_linked_list.pop_first()
        self.assertEqual(my_linked_list.length, 0)
        
    def test_get(self):
        my_linked_list = linked_list.LinkedList(4)
        my_linked_list.append(5)
        my_linked_list.append(6)
        my_linked_list.append(7)
        value = my_linked_list.get(2).value
        self.assertEqual(value, 6)
        
    def test_set(self):
        my_linked_list = linked_list.LinkedList(4)
        my_linked_list.append(5)
        my_linked_list.append(6)
        my_linked_list.set_value(1, 7)
        value = my_linked_list.get(1).value
        self.assertEqual(value, 7)
        self.assertEqual(my_linked_list.length, 3)
        
        
if __name__ == '__main__':
    unittest.main()