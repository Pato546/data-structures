class ArrayStack:
    """This is an array implementation of a **stack** datastructure
    which uses the Adapter Design Pattern.
    """

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return reversed(self._data)

    def push(self, el):
        self._data.append(el)

    def pop(self):
        return self._data.pop(-1)


class LinkedStack:
    class Node:
        __slots__ = "element", "next"

        def __init__(self, elem, next_) -> None:
            self.element = elem
            self.next = next_

    class linked_stack_iterator:
        def __init__(self, __o) -> None:
            self.head = __o.head

        def __iter__(self):
            return self

        def __next__(self):
            try:
                if self.head is None:
                    raise StopIteration
                return self.head
            finally:
                try:
                    self.head = self.head.next
                except AttributeError:
                    raise StopIteration

    def __init__(self) -> None:
        self.head = None
        self.size = 0

    def __iter__(self):
        return self.linked_stack_iterator(self)

    def push(self, elem):
        if self.size == 0:
            self.head = self.Node(elem=elem, next_=None)
        else:
            node = self.Node(elem=elem, next_=self.head)
            self.head = node

        self.size += 1

    def pop(self):
        if self.size == 0:
            return
        head = self.head
        self.head = self.head.next
        self.size -= 1

        return head


l = LinkedStack()
l.push(1)
l.push(2)
l.push(3)
l.pop()
l.pop()
l.pop()

for i in l:
    print(i.element)

exit()


def match_expr(expr: str) -> True:
    left = {"{": 0, "(": 1, "[": 2}
    right = {"}": 0, ")": 1, "]": 2}

    arr = ArrayStack()

    for delimeter in expr:
        if delimeter in left:
            arr.push(delimeter)
        elif delimeter in right:
            if len(arr):
                if left.get(arr.pop()) == right.get(delimeter):
                    continue
                else:
                    return False
            else:
                return False

    return True


if __name__ == "__main__":
    print(match_expr("{(((({{{{}}}}))))}"))
