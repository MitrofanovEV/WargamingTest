class BufferOverflowError(ValueError):
    pass


class QueueIsEmptyError(ValueError):
    pass


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class FIFOCycleBuffer:
    """Linked list implementation"""

    def __init__(self, length):
        self.head = Node(None)
        tmp = self.head
        for i in range(length - 1):
            tmp1 = Node(None)
            self.head.next = tmp1
            self.head = tmp1
        self.head.next = tmp
        self.tail = self.head

    def push(self, val):
        if self.tail.val is not None:
            raise BufferOverflowError()
        self.tail.val = val
        self.tail = self.tail.next

    def pop(self):
        if self.head.val is None:
            raise QueueIsEmptyError()
        tmp = self.head.val
        self.head.val = None
        self.head = self.head.next
        return tmp


class FIFOCycleBuffer1:
    """Array implementation"""

    def __init__(self, length):
        self.buffer = [None] * length
        self.head = 0
        self.tail = 0

    def push(self, val):
        if self.buffer[self.tail] is not None:
            raise BufferOverflowError()
        self.buffer[self.tail] = val
        self.tail = (self.tail + 1) % len(self.buffer)

    def pop(self):
        if self.buffer[self.head] is None:
            raise QueueIsEmptyError()
        tmp = self.buffer[self.head]
        self.buffer[self.head] = None
        self.head = (self.head + 1) % len(self.buffer)
        return tmp



f = FIFOCycleBuffer(500)
"""
При реализации с помощью связного списка образение к конкретному элементу будет за O(n), что неэффективно, 
зато мы имеем оптимальный расход памяти
"""
f1 = FIFOCycleBuffer1(500)
"""
При реализации с помощью списка python list, который на самом деле представляет собой динамический массив,
мы можем обращяться к конкретным элементам за O(1), однако он всегда занимает больше памяти, чем сами элементы
"""