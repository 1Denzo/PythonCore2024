# Создать класс. Очередь на структуре данных двусвязный список. 

class Node:
    # Вспомогательный класс для узлов списка
    def __init__(self, data):
        self.data = data  # храним информацию
        self.nref = None  # ссылка на следующий узел
        self.pref = None  # Ссылка на предыдущий узел


class Queue:
    # Основной класс
    def __init__(self):
        self.start = None  # ссылка на начало очереди
        self.end = None  # ссылка на конец очереди

    def pop(self):
        # Возвращаем элемент val из начала списка с удалением из списка
        if self.is_empty():
            raise IndexError("Очередь пуста")
        val = self.front.value
        self.front = self.front.next
        if self.front is None:  # Если очередь стала пустой
            self.rear = None
        else:
            self.front.prev = None
        return val

    def push(self, val):
        # Добавление элемента val в конец списка
        new_node = Node(val)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node
            
    def insert(self, n, val):
        # Вставить элемент val между элементами с номерами n-1 и n
        new_node = Node(val)
    
        if n <= 0:
                raise IndexError("Индекс должен быть больше 0.")
    
        current = self.front
        index = 0
    
        # Перебираем элементы очереди
        while current is not None and index < n - 1:
            current = current.next
            index += 1
    
        if current is None:
            raise IndexError("Индекс выходит за границы очереди.")
    
    # Вставляем новый узел между элементами
        new_node.prev = current.prev
        new_node.next = current
    
        if current.prev is not None:
            current.prev.next = new_node
        else:
            self.front = new_node  # Если вставляем в начало очереди

        current.prev = new_node
    def print(self):
        # Вывод на печать содержимого очереди
        current = self.front
        items = []
        while current:
            items.append(current.value)
            current = current.next
        print(str(items))
        