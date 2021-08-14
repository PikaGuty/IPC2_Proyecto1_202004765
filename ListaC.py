class ListaCerrada:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.sig = None

    #Métodos GET
    def getX(self):
        return self.x

    def getY(self):
        return self.y

    #Métodos SET
    def setX(self,x):
        self.x = x

    def setY(self,y):
        self.y = y
    
    def setSig(self,sig):
        self.sig = sig

class ListaC:

    def __init__(self):
        self.primero = None

    def insertar(self, nNode):
        if self.primero:
            uNode = self.primero
            while uNode.sig != None:
                uNode = uNode.sig
            uNode.sig = nNode
        else:
            self.primero = nNode
        

    def ExisteCoordenada(self,x,y):
        tNode = self.primero
        c=1
        while tNode != None:
            if x==tNode.getX() and y==tNode.getY():
                
                return False
            tNode = tNode.sig
        
        return True

    def mostrar(self):
        tNode = self.primero

        while tNode != None:
            print("("+str(tNode.getX())+" , "+str(tNode.getY())+")", end='->')
            tNode = tNode.sig

        print('Null')

    def EliminarU(self):
        tNode = self.primero
        ttNode=None
        while tNode != None:
            tttNode=ttNode
            ttNode=tNode
            tNode = tNode.sig
        tttNode.sig=None
        
