class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data=None):
        self.data = data
        self.next_node = None


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        self.head = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        if not self.head:
            self.head = Node(data)
            return

        current = self.head

        self.head = Node(data)
        self.head.next_node = current

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.next_node:
            current = current.next_node
        current.next_node = Node(data)

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f'{str(node.data)} -> '
            node = node.next_node

        ll_string += 'None'
        return ll_string
