class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None
        self.size = 0
        self.list_of_data = []

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        tmp = Node(data, None)
        if self.size == 0:
            self.head = tmp
        else:
            self.tail.next_node = tmp
        self.tail = tmp
        self.size += 1
        self.list_of_data.append(data)

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if self.head is None:
            return None
        result = self.head.data
        self.head = self.head.next_node
        self.size -= 1
        if self.head is None:
            self.tail = None
        return result

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        if self.size == 0:
            return f""
        else:
            return "\n".join(map(str, self.list_of_data))
