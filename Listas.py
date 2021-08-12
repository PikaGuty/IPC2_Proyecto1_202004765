

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaE:
    def __init__(self):
        self.head = None

    def insertar(self, nuevo):
        if self.head:
            ultimo = self.head
            while ultimo.siguiente != None:
                ultimo = ultimo.siguiente
            ultimo.siguiente = nuevo
        else:
            self.head = nuevo

    def mostrar(self):
        temp = self.head
        while temp != None:
            print(temp.dato, end='->')
            temp = temp.siguiente
        print('Null')

    def longitud(self):
        temp = self.head
        l=0
        while temp != None:
            l+=1
            temp = temp.siguiente
        return l

    def ordenar(self):
        temp = self.head
        l=longitud()
        for x in range(l):
            while temp != None:
                insertar(Nodo(1))
                print(temp.dato, end='->')
                temp = temp.siguiente
            print('Null')


if __name__ == '__main__':
    lista = ListaE()

    lista.insertar(Nodo(1))
    lista.insertar(Nodo(2))
    lista.insertar(Nodo(3))
    lista.insertar(Nodo(4))
    lista.insertar(Nodo(5))
    lista.insertar(Nodo(6))
    lista.insertar(Nodo(7))

    lista.mostrar()
    print(lista.longitud())