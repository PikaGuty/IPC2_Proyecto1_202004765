from ObjTerreno import Terreno
from P1_OP1 import op1

class op2:
    def ProcesarTerreno(Terrenos):
        Ter=Terrenos
        for t in Ter:
            print(t.getNombre())
            print(t.getInicio())
            print(t.getFin())
            print(t.getDimc())
            print(t.getDimf())
            print(t.getGas())
