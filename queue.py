from collections import deque


class DequeQueue:
    """This is a implementation of a **queue** datastructure"""

    def __init__(self):
        self._data = deque()

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self._data)

    def enqueue(self, el):
        self._data.append(el)

    def dequeue(self):
        return self._data.popleft()


class LinkedQueue:
    """This is a linked list implementation of a **queue** datastructure"""

    class Node:
        __slots__ = "element", "next"

        def __init__(self, elem, next_) -> None:
            self.element = elem
            self.next = next_


    class linked_queue_iterator:
        
        def __init__(self, __o) -> None:
            self.head = __o.head

        def __iter__(self):
            return self

        def __next__(self):
            try:
                if self.head is None:
                    raise StopIteration
                return self.head.element
            finally:
                try:
                    self.head = self.head.next
                except AttributeError:
                    raise StopIteration

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self) -> int:
        return self.size

    def __iter__(self):
        return self.linked_queue_iterator(self)

    def enqueue(self, el):
        node = self.Node(el, None)

        if self.size == 0:
            self.tail = node
            self.head = node

        else:
            self.tail.next = node
            self.tail = node

        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return

        head = self.head

        if self.size == 1:
            self.head = self.head.next
            self.tail = self.head

        else:
            self.head = self.head.next

        self.size -= 1

        return head.element


if __name__ == "__main__":

    dq = LinkedQueue()

    dq.enqueue(1)
    dq.enqueue(2)
    dq.enqueue(3)

    for e in dq:
        print(e)
