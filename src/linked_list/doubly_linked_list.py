class DoublyLinkedList:
    class Node:

        __slots__ = "_prev", "_element", "_next"

        def __init__(self, prev, element, next_):
            self._prev = prev
            self._element = element
            self._next = next_

    def __init__(self):
        self.header = self.Node(None, None, None)
        self.trailer = self.Node(None, None, None)

        self.header._next = self.trailer
        self.trailer._prev = self.header

        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def _insert_between(self, e, predecessor, successor):
        new_node = self.Node(predecessor, e, successor)

        predecessor._next = new_node
        successor._prev = new_node

        self.size += 1

        return new_node

    def _delete_node(self, node):
        previous_node = node._prev
        next_node = node._next

        previous_node._next = next_node
        next_node._prev = previous_node

        self.size -= 1

        e = node._element

        node._prev = None
        node._next = None
        node._element = None

        return e

    def insert_first(self, e):
        self._insert_between(e, self.header, self.header._next)

    def insert_last(self, e):
        self._insert_between(e, self.trailer._prev, self.trailer)

    def delete(self, node):
        return self._delete_node(node)


if __name__ == "__main__":
    dl = DoublyLinkedList()

    dl.insert_last(2)
    dl.insert_first(1)

    print(len(dl))

    while dl.header._next is not None:
        print(dl.header._next._element)
        dl.header._next = dl.header._next._next
