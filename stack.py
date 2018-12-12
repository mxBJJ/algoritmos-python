class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, x):
        # insere um elemento na pilha
        node = Node(x)
        node.next = self.top
        self.top = node
        self._size = self._size + 1

    def pop(self):
        # remove o elemento do topo da pilha
        if self._size > 0:
            node = self.top
            self.top = self.top.next
            self._size = self._size - 1
            return node.data
        raise IndexError("The stack is empty.")

    def peek(self):
        # retorna o topo sem remover
        if self._size > 0:
            return self.top.data
        raise IndexError("The stack is empty.")

    def __len__(self):
        return self._size

    def __repr__(self):
        r = ""
        pointer = self.top
        while(pointer):
            r = r + str(pointer.data) + "\n"
            pointer = pointer.next
        return r

    def __str__(self):
        print("="*80)
        print("Pilha:")
        print("="*80)
        print("\n")
        return self.__repr__()


class Main:
        pilha = Stack()
        pilha.push(5)
        pilha.push(7)
        pilha.push(9)
        print("Stack size: {}".format(len(pilha)))
        print(str(pilha))
