from node import Node

class LinkeList:
    def __init__(self):
        self.head = None
        self.size = 0

        def append(self, elem):
            if self.head:
                pass
            else:
                #Primeira inserção
                self.head = Node(elem)

lista = LinkeList()