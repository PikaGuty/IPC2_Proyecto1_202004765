class Terreno:
    def __init__(self,nombre,inicio,fin,gas):
        self.nombre = nombre
        self.inicio = inicio
        self.fin = fin
        self.gas = gas
        
        
        g=list(gas.items())[-1]
        gg=str(g).split(",")
        #print(gg)

        self.dimc = int((gg[0].split("\'"))[1])
        self.dimf = int((gg[1].split("\'"))[0])
        print(str(nombre)+" Guardado con éxito")

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

    
    
