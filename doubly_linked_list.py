class DoublyLinkedList():

    class _Node():

        def __init__(self, value):
            self._value = value
            self._next = None
            self._prev = None

    def __init__(self, seq=()):
        self._head = None
        self._tail = None
        self._size = 0  # set default values

        self.extend(seq)  # copy iterables values

    def __iter__(self):
        node = self._head
        while node:
            yield node._value
            node = node._next

    def __len__(self):
        return self._size

    def __str__(self):

        return 'None <= ' + ' <=> '.join(map(str, self)) + ' => None'

    def __repr__(self):
        return self.__str__()

    def __contains__(self, item):

        for i in self:
            if i == item:
                return True
        return False

    def __eq__(self, other):

        if type(other) is not type(self):  # check if other is dll
            return False
        if len(self) != len(other):
            return False
        for i, j in zip(self, other):
            if i != j:
                return False
        return True

    def __getitem__(self, index):
        # change index if negative
        index = self._size + index if index < 0 else index
        if 0 <= index < self._size:
            for i, item in enumerate(self):
                if i == index:
                    return item
        else:
            raise IndexError('list index out of range')

    def __setitem__(self, index, item):
        # change index if negative
        index = self._size + index if index < 0 else index
        if 0 <= index < self._size:
            i = 0
            node = self._head
            while i < index:
                node = node._next
                i += 1
            node._value = item
        else:
            raise IndexError('list assignment index out of range')

    def __delitem__(self, index):
        # change index if negative
        if type(index) is not int:
            raise TypeError('list index must be an integer')

        index = self._size + index if index < 0 else index
        if 0 < index < self._size - 1:
            i = 0
            node = self._head
            while i < index:
                node = node._next
                i += 1
            node._prev._next = node._next
            node._next._prev = node._prev
            self._size -= 1
        elif index == 0 and self._head is not None:  # case for head
            self._head = self._head._next
            self._head._prev = None
            self._size -= 1
        elif index == self._size - 1 and self._head is not None:
            self._tail = self._tail._prev
            self._tail._next = None
            self._size -= 1
        else:
            raise IndexError('list index out of range')

    def insertStart(self, item):

        new_node = self._Node(item)
        if not self._head:  # or if not self._tail
            self._head = new_node
            self._tail = new_node
        else:
            new_node._next = self._head
            self._head._prev = new_node
            self._head = new_node
        self._size += 1

    def insertEnd(self, item):
        new_node = self._Node(item)
        if not self._tail:  # or if not self._head
            self._tail = new_node
            self._head = new_node
        else:
            new_node._prev = self._tail
            self._tail._next = new_node
            self._tail = new_node
        self._size += 1

    def insert(self, index, item):

        t = type(index)
        if t is not int:
            raise TypeError('{} cannot be interpreted as an integer'.format(t))
        else:
            # change index if negative
            index = self._size + index if index < 0 else index
            if index > self._size - 1:  # check for special cases
                self.insertEnd(item)
            elif index <= 0:
                self.insertStart(item)
            else:  # iterate through and insert item
                i = 0
                node = self._head
                while i < index - 1:
                    node = node._next
                    i += 1
                new_node = self._Node(item)
                new_node._next = node._next
                new_node._prev = node
                node._next = new_node
                new_node._next._prev = new_node
                self._size += 1

    def extend(self, seq=()):

        for i in seq:
            self.insertEnd(i)

    def remove(self, item):

        if not self._head:
            raise IndexError("remove from an empty list")
        else:
            if self._head._value == item:  # case for head
                self._head = self._head._next
                self._head._prev = None
            elif self._tail._value == item:  # case for tail
                self._tail = self._tail._prev
                self._tail._next = None
            else:
                node = self._head
                try:
                    while node._value != item:
                        node = node._next
                    node._prev._next = node._next
                    node._next._prev = node._prev
                except AttributeError:  # mute the original error
                    raise ValueError('value not present in list') from None
            self._size -= 1

    def pop(self, index=-1):

        if self._size == 0:
            raise IndexError("pop from an empty list")
        t = type(index)
        if t is not int:
            raise TypeError('{} cannot be interpreted as an integer'.format(t))
        item = self[index]
        del self[index]
        return item

    def index(self, item):

        for index, el in enumerate(self):
            if el == item:
                return index
        return -1

    def count(self, item):
        """Return number of occurrences of item."""
        count = 0
        for i in self:
            if i == item:
                count += 1
        return count

    def clear(self):
        """Remove all the items from the list."""
        self._head = None
        self._tail = None
        self._size = 0

    def reverse(self):
        """Reverse list in place."""
        tmp = None
        curr = self._head

        while curr:
            tmp = curr._prev
            curr._prev = curr._next
            curr._next = tmp
            curr = curr._prev

        if tmp:
            self._head = tmp._prev

    def sort(self):
        """Sort list in place."""
        self._head = self._merge_sort(self._head)

    def _merge(self, left, right):
        t_head = self._Node(None)
        curr = t_head

        while left and right:
            if left._value < right._value:
                curr._next = left
                left = left._next
            else:
                curr._next = right
                right = right._next
            curr = curr._next

        if left is None:
            curr._next = right
        if right is None:
            curr._next = left

        return t_head._next

    def _split(self, lst):
        if lst is None or lst._next is None:
            left = lst
            right = None
            return left, right
        else:
            mid = lst
            fast = lst._next

            while fast is not None:
                fast = fast._next

                if fast is not None:
                    fast = fast._next
                    mid = mid._next
        left = lst
        right = mid._next
        mid._next = None

        return left, right

    def _merge_sort(self, t_head):
        if t_head is None:
            return t_head
        if t_head._next is None:
            return t_head

        left, right = self._split(t_head)
        left = self._merge_sort(left)
        right = self._merge_sort(right)

        return self._merge(left, right)


if __name__ == '__main__':
    dll = DoublyLinkedList([12, 16, 21, 83, 77, 90])
    print(dll)
    dll.insertEnd(4)
    dll.insertStart(0)
    dll.sort()
    dll.insert(-13, 'start')
    print(dll)
    print(dll.pop())
    print(dll.pop(2))
    dll.remove(4)
    dll.extend('iterable')
    dll.index(8)
    print(dll.count(4))
    print(dll)
