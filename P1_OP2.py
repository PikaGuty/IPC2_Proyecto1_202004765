from ObjTerreno import Terreno
from P1_OP1 import op1
from ObjRuta import Ruta



class op2:
    def ProcesarTerreno(Terrenos):
        Ter=Terrenos
        c=0      
        for t in Ter:
            c+=1
        seleccion = 0
        while seleccion != (c+1):
            print('***************************************************************\n'+
                '**         SELECCIONE EL TERRENO QUE DESEA PROCESAR          **\n'+
                '***************************************************************')
            c=0      
            for t in Ter:
                c+=1
                print("**  {:<4}{:<51}  **".format((str(c)+"."),t.getNombre()))

            print("**  {:<4}{:<51}  **".format((str(c+1)+"."),"Regresar al menú principal"))    
            print('***************************************************************')
            try:
                seleccion = int(input())
            except:
                print("Debe ingresar un número")
            if seleccion==(c+1):
                break

            #Nombre terreno
            NomT=Ter[seleccion-1].getNombre()
            #Coordenada de inicio
            CInicio=Ter[seleccion-1].getInicio()
            #Coordenada final
            CFinal=Ter[seleccion-1].getFin()
            #Dimension de Columnas
            DimC=Ter[seleccion-1].getDimc()
            #Dimension de Filas
            DimF=Ter[seleccion-1].getDimf()
            #Diccionario de Coordenadas con su gasto de gasolina 
            CmGas=Ter[seleccion-1].getGas()

            gas=list(CmGas.items())
            gasolina=[]
            Fila=[]
            MatrizG=[]
            
            for y in gas:
                gasolina.append(y[1])
            
            c=0
            for x in range(DimF):
                Fila=[]
                for y in range(DimC):
                    Fila.append(gasolina[y+(DimC*c)])
                MatrizG.append(Fila)
                c+=1
            print("\n\nMatriz de Gasolina para "+NomT+"\n")
            for x in MatrizG:
                print(x)
            print("\n\nCoordenadas de Inicio:")
            print(CInicio)
            print("Coordenadas Finales:")
            print(CFinal)

            CActual=CInicio

            CActual=[CActual[1]-1,CActual[0]-1]
            CFinal=[CFinal[1]-1,CFinal[0]-1]

            ListaC=[]
            Gasolina=0
            
            while CActual!=CFinal:
                sup=[]
                inf=[]
                der=[]
                izq=[]
                if CActual[0]>=0 and CActual[1]-1>=0 and [int(CActual[0]),int(CActual[1]-1)] not in ListaC:
                    distancia=abs(CFinal[0]-CActual[0])+abs(CFinal[1]-int(CActual[1]-1))
                    izq.append(MatrizG[int(CActual[0])][int(CActual[1]-1)]+distancia)
                    cizq=[int(CActual[0]),int(CActual[1]-1)]
                    izq.append(cizq)
                else:
                    izq=[9999,[1000,1000]]
                if CActual[0]>=0 and CActual[1]+1<DimC and [int(CActual[0]),int(CActual[1]+1)] not in ListaC:
                    distancia=abs(CFinal[0]-CActual[0])+abs(CFinal[1]-int(CActual[1]+1))
                    der.append(MatrizG[int(CActual[0])][int(CActual[1]+1)]+distancia)
                    cder=[int(CActual[0]),int(CActual[1]+1)]
                    der.append(cder)
                else:
                    der=[9999,[1000,1000]]
                if CActual[1]>=0 and CActual[0]-1>=0 and [int(CActual[0]),int(CActual[1])] not in ListaC:
                    distancia=abs(CFinal[0]-int(CActual[0]-1))+abs(CFinal[1]-int(CActual[1]))
                    sup.append(MatrizG[int(CActual[0]-1)][int(CActual[1])]+distancia)
                    csup=[int(CActual[0]-1),int(CActual[1])]
                    sup.append(csup)
                else:
                    sup=[9999,[1000,1000]]
                if CActual[1]>=0 and CActual[0]+1<DimF and [int(CActual[0]+1),int(CActual[1])] not in ListaC:
                    distancia=abs(CFinal[0]-int(CActual[0]+1))+abs(CFinal[1]-int(CActual[1]))
                    inf.append(MatrizG[int(CActual[0]+1)][int(CActual[1])]+distancia)
                    cinf=[int(CActual[0]+1),int(CActual[1])]
                    inf.append(cinf)
                else:
                    inf=[9999,[1000,1000]]
                
                ord=[sup,inf,izq,der]
                print(ord)
                asc=sorted(ord, key=lambda gas: gas[0])
                cop=asc[0][1]
                print(cop)
                opp1=int(MatrizG[int(cop[0])][int(cop[1])])
                print("Nueva coordenada "+str(cop)+" Gasto de Gasolina "+str(opp1))
                ListaC.append(cop)
                CActual=cop


                
                
                







