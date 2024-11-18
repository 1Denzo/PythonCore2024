# Создать класс Cтек на структуре данных Односвязный список. 

class Node:
    # Вспомогательный класс для узлов списка
    def __init__(self, data):
        self.data = data  # храним информацию
        self.pref = None  # ссылка на предыдущий узел

class Stack:
    # Основной класс для стека
    def __init__(self):
        self.end = None  # ссылка на конец стека

    def pop(self):
        # Возвращение последнего элемента из списка с удалением его из списка
        if self.is_empty():
            raise IndexError("Стек пуст")
        val = self.top.value
        self.top = self.top.next
        return val

    def push(self, val):
        # Добавление элемента val в конец списка
        new_node = Node(val)
        if self.is_empty():
            self.top = new_node
            self.bottom = new_node
        else:
            self.bottom.next = new_node
            self.bottom = new_node
    def print(self):
        # Вывод на печать содержимого стека
        current = self.top
        items = []
        while current:
            items.append(current.value)
            current = current.next
        return items[::-1]  # возвращаем список в правильном порядке

