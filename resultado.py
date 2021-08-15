class Resultado:
    def __init__(self,nombre,pix,piy,pfx,pfy,dimc,dimf,gas,recorrido):
        self.nombre = nombre
        #Posicion inicial
        self.pix = pix
        self.piy = piy
        #Posicion final
        self.pfx = pfx
        self.pfy = pfy
        #Dimensiones
        self.dimc = dimc
        self.dimf = dimf
        #Gas total
        self.gas = gas
        #Lista recorrido
        self.recorrido = recorrido

        self.sig = None

    #Métodos GET
    def getNombre(self):
        return self.nombre
    
    def getPix(self):
        return self.pix
    
    def getPiy(self):
        return self.piy
    
    def getPfx(self):
        return self.pfx
    
    def getPfy(self):
        return self.pfy
    
    def getDimc(self):
        return self.dimc

    def getDimf(self):
        return self.dimf

    def getGas(self):
        return self.gas

    def getRecorrido(self):
        return self.recorrido

    def getSig(self):
        return self.sig

    #Métodos SET
    def setNombre(self,nombre):
        self.nombre = nombre

    def setPix(self,pix):
        self.pix = pix

    def setPiy(self,piy):
        self.piy = piy

    def setPfx(self,pfx):
        self.pfx = pfx

    def setPfy(self,pfy):
        self.pfy = pfy

    def setDimc(self,dimc):
        self.dimc = dimc

    def setDimf(self,dimf):
        self.dimf = dimf

    def setRecorrido(self,recorrido):
        self.recorrido = recorrido

    def setGas(self,gas):
        self.gas = gas

    def setSig(self,sig):
        self.sig = sig

class ListaR:

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

    def bus(self, nombre):
        tNode = self.primero
        while tNode != None:
            if nombre == tNode.getNombre():
                return False
            tNode = tNode.sig
        return True

    def retornar_seleccionado(self, n):
        tNode = self.primero
        c=1
        while tNode != None:
            if n is c:
                return tNode
            tNode = tNode.sig
            c+=1

    def longitud(self):
        tNode = self.primero
        c=0
        while tNode != None:
            c+=1
            tNode = tNode.sig

        return c

    def mostrarM(self):
        tNode = self.primero
        c=1
        while tNode != None:
            print("**  {:<4}{:<51}  **".format((str(c)+"."),tNode.getNombre()))
            tNode = tNode.sig
            c+=1
        

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
            print(str(tNode.getNombre()), end='->')
            tNode = tNode.sig

        print('Null')