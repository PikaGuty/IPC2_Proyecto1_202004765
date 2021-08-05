class Terreno:
    def __init__(self,nombre,inicio,fin,dimc,dimf,gas):
        self.nombre = nombre
        self.inicio = inicio
        self.fin = fin
        self.dimc = dimc
        self.dimf = dimf
        self.gas = gas

    #Métodos GET
    def getNombre(self):
        return self.nombre

    def getInicio(self):
        return self.inicio

    def getFin(self):
        return self.fin
    
    def getDimc(self):
        return self.dimc

    def getDimf(self):
        return self.dimf

    def getGas(self):
        return self.gas

    #Métodos SET
    def setNombre(self,nombre):
        self.nombre = nombre

    def setInicio(self,inicio):
        self.inicio = inicio

    def setFin(self,fin):
        self.fin = fin

    def setDimc(self,dimc):
        self.dimc = dimc

    def setDimf(self,dimf):
        self.dimf = dimf

    def setGas(self,gas):
        self.gas = gas

    
    
