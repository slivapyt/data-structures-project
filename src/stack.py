class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""

    def __init__(self):
        self.top = None
        """Конструктор класса Stack"""

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        next_node = self.top
        new_top = Node(data, next_node)
        self.top = new_top

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        if self.top is None:
            return None
        data = self.top.data
        self.top = self.top.next_node
        return data

    def peek(self):
        return self.top.data if self.top is not None else None

    def __str__(self):
        return f'{self.data}'
