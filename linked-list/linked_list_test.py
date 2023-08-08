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
        
        
if __name__ == '__main__':
    unittest.main()