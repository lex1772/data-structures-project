"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Node, Stack


class TestSrc(unittest.TestCase):
    def test_node_init(self):
        n1 = Node(5, None)
        self.assertEqual(n1.data, 5)
        self.assertEqual(n1.next_node, None)

    def test_stack_push(self):
        stack = Stack()
        stack.push('data1')
        self.assertEqual(stack.top.data, 'data1')

    def test_stack_pop(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        self.assertEqual(stack.pop(), 'data2')

    def test_str(self):
        stack = Stack()
        stack2 = Stack()
        stack.push('data1')
        self.assertEqual(str(stack), 'data1')
        with self.assertRaises(Exception):
            stack2.pop()
        self.assertEqual(str(stack2), '')


if __name__ == '__main__':
    unittest.main()
