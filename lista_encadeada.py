class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def getSize(self):
        return self.size

    def myFirst(self):
        first = self.head
        print("Primeiro: {}".format(self.head.data))

    def myLast(self):
        last = self.tail
        print("Ultimo: {}".format(self.tail.data))

    def myAppend(self, x):
        if self.tail is None:
            self.head = self.tail = Node(x)
        else:
            self.tail.next = Node(x)
            self.tail = self.tail.next

    def showList(self):
        i = self.head
        while i is not None:
                if(i.next is not None):
                    print(i.data, end=" -> ")
                else:
                    print(i.data)
                i = i.next
        print("\n")


class Main:

    lista = LinkedList()
    lista.myAppend(5)
    lista.myAppend(6)
    lista.myAppend(9)
    lista.myAppend("python")
    lista.myAppend(22)
    lista.showList()
    lista.myFirst()
    lista.myLast()
