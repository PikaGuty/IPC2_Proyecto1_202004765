class Ruta:
    def __init__(self,Gacum,Cant,Noit):
        self.Gacum = Gacum
        self.Cant = Cant
        self.Noit = Noit

    #Métodos GET
    def getGacum(self):
        return self.Gacum

    def getInicio(self):
        return self.inicio

    def getNoit(self):
        return self.Noit

    #Métodos SET
    def setGacum(self,Gacum):
        self.Gacum = Gacum

    def setCant(self,Cant):
        self.Cant = Cant

    def setNoit(self,Noit):
        self.Noit = Noit