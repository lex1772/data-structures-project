"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest
from src.linked_list import Node, LinkedList

class TestSrc(unittest.TestCase):
    def test_node_init(self):
        n1 = Node({'id': 1}, None)
        self.assertEqual(n1.data, {'id': 1})
        self.assertEqual(n1.next_node, None)

    def test_insert_beginning(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        self.assertEqual(str(ll), "{'id': 1} -> None")
        ll.insert_beginning({'id': 0})
        self.assertEqual(str(ll), "{'id': 0} -> {'id': 1} -> None")


    def test_insert_at_end(self):
        l = LinkedList()
        l.insert_at_end({'id': 2})
        self.assertEqual(str(l), "{'id': 2} -> None")
        l.insert_beginning({'id': 1})
        l.insert_beginning({'id': 0})
        l.insert_at_end({'id': 3})
        self.assertEqual(str(l), "{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None")