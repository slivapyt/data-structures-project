class Node:
    """Класс для узла очереди"""

    def __init__(self, data=None, next_node=None):
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

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь
        :param data: данные, которые будут добавлены в очередь
        """

        temp_node = Node(data, None)
        if self.head is None:
            self.head = temp_node
            self.tail = self.head
        else:
            self.tail.next_node = temp_node
            self.tail = temp_node

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if self.head is None:
            return None
        else:
            data = self.head.data
            self.head = self.head.next_node
            if self.head is None:
                self.tail = None
            return data

    def __str__(self):
        return ""
