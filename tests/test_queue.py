"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest
from src.queue import Node, Queue


class TestSrc(unittest.TestCase):
    def test_node_init(self):
        n1 = Node(5, None)
        self.assertEqual(n1.data, 5)
        self.assertEqual(n1.next_node, None)

    def test_queue_enqueue(self):
        queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')
        self.assertEqual(str(queue), 'data1\ndata2\ndata3')
        self.assertEqual(queue.head.next_node.data, 'data2')

    def test_queue_dequeue(self):
        queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')
        self.assertEqual(queue.dequeue(), 'data1')


if __name__ == '__main__':
    unittest.main()
