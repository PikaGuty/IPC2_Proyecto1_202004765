class MOrto:
    #Ininicializando nodo
    def __init__(self):
        self.iNodo = None
    #Función Insertar
    def insertar(self,nodoNuevo):
        #Si no existe ningun nodo, se inserta el nuevo para iniciar la lista
        if self.iNodo is None:
            nNode = nodoNuevo
            self.iNodo = nNode
        else:
            #Tomando el valor Y del nuevo nodo ingresado, se determina si ingresarlo en la misma fila del ya existente
            if nodoNuevo.getY() == 0:
                n = self.iNodo
                while n.derecha is not None:
                    n = n.derecha
                nNode = nodoNuevo
                n.derecha = nNode
                nNode.izquierda = n
            #Si no pertenece a la misma fila, se crea una nueva con este nodo
            else:
                n = self.iNodo
                while n.abajo is not None:
                    n = n.abajo
                # Si X=0 se crea el nuevo nodo debajo del primero que se insertó
                if nodoNuevo.getX() == 0:
                    nNode = nodoNuevo
                    n.abajo = nNode
                    nNode.arriba = n
                #De lo contrario se debe obtener el nodo que se encuentra arriba de la posición que corresponde
                #para enlazarlo con el nuevo
                else:
                    while n.derecha is not None:
                        n = n.derecha
                    nNode = nodoNuevo
                    n.derecha = nNode
                    nNode.izquierda = n
                    nodoA = self.obtener(nNode.getX(), nNode.getY()-1)
                    nodoA.abajo = nNode
                    nNode.arriba = nodoA

    #Obtener valor por "x" y "y"
    def obtener(self, x, y):
        n = self.iNodo
        while n.getX() < x:
            n = n.derecha
        while n.getY() < y:
            n = n.abajo
        return n

    #Obtener toda la matriz ingresada
    def recorrer(self):
        if self.iNodo is None:
            print("Lista sin elementos")
            return
        else:
            m = self.iNodo
            while m is not None:
                n = m
                while n is not None:
                    print(str(n.dato),end=",")
                    n = n.derecha
                print('')
                m = m.abajo

    def bus(self, nombre):
        tNode = self.iNodo
        while tNode != None:
            if nombre == tNode.getNombre():
                return tNode
            tNode = tNode.sig
        return None

    

 
    