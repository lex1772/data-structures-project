class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс для односвязного списка"""
    head = None
    end = None
    elements_list = []

    def __init__(self):
        self.elements_list = []

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        tmp = Node(data)
        if self.head is None:
            self.head = tmp
            self.end = self.head
        else:
            tmp.next_node = self.head
        self.head = tmp
        self.elements_list.insert(0, data)

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        tmp = Node(data)
        if self.head is None:
            self.head = tmp
            self.end = self.head
        else:
            self.end.next_node = tmp
        self.end = tmp
        self.elements_list.append(data)

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        return ll_string.lstrip()

    def to_list(self):
        return self.elements_list

    def get_data_by_id(self, key):
        while key <= len(self.elements_list):
            try:
                if not isinstance(self.elements_list[key], dict):
                    key += 1
                    raise TypeError
            except TypeError:
                print('Данные не являются словарем или в словаре нет id.')
            else:
                return self.elements_list[key]
        else:
            print('Данные не являются словарем или в словаре нет id.')
