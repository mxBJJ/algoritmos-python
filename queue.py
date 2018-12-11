class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def push(self, x):
        # insere um elemento na pilha
        node = Node(x)
        if self.last is None:
            self.last = node

        else:
            self.last.next = node
            self.last = node

        if self.first is None:
            self.first = node

        self.size = self.size + 1

    def pop(self):
        # remove o elemento do topo da pilha
        if self.size > 0:
            elemento = self.first.data
            self.first = self.first.next
            self.size = self.size - 1
            return elemento
        else:
            print("The queue is empty")

    def peek(self):
        # retorna o topo sem remover
        if self.size > 0:
            elemento = self.first.data
            return elemento
        else:
            print("The queue is empty")

    def __len__(self):
        print("="*80)
        print("Fila:")
        print("="*80)
        print("\n")
        return self._size

    def __repr__(self):
        if self.size > 0:
            r = ""
            pointer = self.first
            while(pointer):
                r = r + str(pointer.data) + " -> "
                pointer = pointer.next
        return r

    def __str__(self):
        print("="*80)
        print("Fila:")
        print("="*80)
        print("\n")
        return self.__repr__()


class Main:
        fila = Queue()
        fila.push(5)
        fila.push(3)
        fila.push(9)
        print("Queue size: {}".format(str(fila)))
