"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Node, Stack


class TestSrc(unittest.TestCase):
    def test_node_init(self):
        n1 = Node(5, None)
        self.assertEqual(n1.data, 5)
        self.assertEqual(n1.next_node, None)

    def test_stack_pust(self):
        stack = Stack()
        stack.push('data1')
        self.assertEqual(stack.top.data, 'data1')

    def test_stack_pop(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        self.assertEqual(stack.pop(), 'data2')


if __name__ == '__main__':
    unittest.main()
