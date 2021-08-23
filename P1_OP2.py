from ObjTerreno import Terreno
from P1_OP1 import op1
from ObjTerreno import Lista
from MOrto import MOrto
from NOrtogonal import NodoOrtogonal
from ListaC import ListaCerrada
from ListaC import ListaC
from resultado import Resultado
from resultado import ListaR


class op2:
    def ProcesarTerreno(Terrenos):
        Ter=Terrenos
        c=Ter.longitud()
        seleccion = 0
        ListaRR=ListaR()
        while seleccion != (c+1):
            c=Ter.longitud()
            print("\n\n\n")
            print('***************************************************************\n'+
                '**         SELECCIONE EL TERRENO QUE DESEA PROCESAR          **\n'+
                '***************************************************************')
            Ter.mostrarM()
            print("**  {:<4}{:<51}  **".format((str(c+1)+"."),"Regresar al menú principal"))    
            print('***************************************************************')
            try:
                seleccion = int(input())
            except:
                print("Debe ingresar un número")
            if seleccion==(c+1):
                break
            elif seleccion>(c+1):
                print("Seleccione un numero del menú")
                continue
            try:
                Terr = Ter.retornar_seleccionado(seleccion)
            except:
                break

            #Nombre terreno
            NomT=Terr.getNombre()

            #Coordenada de inicio
            CPiy=int(Terr.getPix())-1
            CPix=int(Terr.getPiy())-1
            #Coordenada final
            CPfy=int(Terr.getPfx())-1
            CPfx=int(Terr.getPfy())-1

            #Dimension de Columnas
            DimC=Terr.getDimc()
            #Dimension de Filas
            DimF=Terr.getDimf()
            #Diccionario de Coordenadas con su gasto de gasolina 
            CmGas=Terr.getGas()

            #print("Nombre "+str(NomT)+" Inicio "+str(CPix+","+CPiy)+" Final "+str(CPfx+","+CPfy)+" DimColumnas "+str(DimC)+"DimFilas"+str(DimF)+" Gasolina ")
            
            print("\n\nMatriz de Gasolina para "+NomT+"\n")
            CmGas.recorrer()
            print("\n\nCoordenadas de Inicio:")
            print(str(CPix)+","+str(CPiy)+"\n")
            print("Coordenadas Finales:")
            print(str(int(CPfx))+","+str(int(CPfy))+"\n")
            #Estableciendo coordenadas iniciales como actuales
            CAx=CPix
            CAy=CPiy

            
            ListaCC = ListaC()
            #ListaCC.insertar(ListaCerrada(int(CAy)-1,int(CAx)-1))
            
            
            
            #print(ListaCC.ExisteCoordenada(CPiy,CPix))

            print("Limites "+str(int(DimF)-1)+" , "+str(int(DimC)-1)+"\n")

            
#*******************************************************************************************************************         
            Gasolina=0
            cont=0
            while CAy!=CPfy or CAx!=CPfx:
                cont+=1
                #Guardando gasolina del punto en el que se encuentra
                Gasolina+=CmGas.obtener(int(CAx),int(CAy)).getDato()
                ListaCC.insertar(ListaCerrada(int(CAx),int(CAy)))
                disD=110
                disI=110
                disA=110
                disAb=110
                #Arriba
                try:
                    if ListaCC.ExisteCoordenada(CmGas.obtener(int(CAx),int(CAy)).arriba.getX(),CmGas.obtener(int(CAx),int(CAy)).arriba.getY()):
                        gasA=CmGas.obtener(int(CAx),int(CAy)).arriba.getDato()
                        disA=abs(int(CPfx)-CmGas.obtener(int(CAx),int(CAy)).arriba.getX())+abs(int(CPfy)-CmGas.obtener(int(CAx),int(CAy)).arriba.getY())
                        futA=op2.EvaluarFuturo(ListaCC,CmGas,CmGas.obtener(int(CAx),int(CAy)).arriba.getX(),CmGas.obtener(int(CAx),int(CAy)).arriba.getY(),CPfx,CPfy)
                        arriba=gasA+disA+futA
                    else:
                        arriba=999
                except:
                    arriba=999
                #Abajo
                try:
                    if ListaCC.ExisteCoordenada(CmGas.obtener(int(CAx),int(CAy)).abajo.getX(),CmGas.obtener(int(CAx),int(CAy)).abajo.getY()):
                        gasAb=CmGas.obtener(int(CAx),int(CAy)).abajo.getDato()
                        disAb=abs(int(CPfx)-CmGas.obtener(int(CAx),int(CAy)).abajo.getX())+abs(int(CPfy)-CmGas.obtener(int(CAx),int(CAy)).abajo.getY())
                        futAb=op2.EvaluarFuturo(ListaCC,CmGas,CmGas.obtener(int(CAx),int(CAy)).abajo.getX(),CmGas.obtener(int(CAx),int(CAy)).abajo.getY(),CPfx,CPfy)
                        abajo=gasAb+disAb+futAb
                    else:
                        abajo=999
                except:
                    abajo=999
                #Izquierda
                try:
                    if ListaCC.ExisteCoordenada(CmGas.obtener(int(CAx),int(CAy)).izquierda.getX(),CmGas.obtener(int(CAx),int(CAy)).izquierda.getY()):
                        gasI=CmGas.obtener(int(CAx),int(CAy)).izquierda.getDato()
                        disI=abs(int(CPfx)-CmGas.obtener(int(CAx),int(CAy)).izquierda.getX())+abs(int(CPfy)-CmGas.obtener(int(CAx),int(CAy)).izquierda.getY())
                        futI=op2.EvaluarFuturo(ListaCC,CmGas,CmGas.obtener(int(CAx),int(CAy)).izquierda.getX(),CmGas.obtener(int(CAx),int(CAy)).izquierda.getY(),CPfx,CPfy)
                        izquierda=gasI+disI+futI
                    else:
                        izquierda=999
                except:
                    izquierda=999
                #Derecha
                try:
                    if ListaCC.ExisteCoordenada(CmGas.obtener(int(CAx),int(CAy)).derecha.getX(),CmGas.obtener(int(CAx),int(CAy)).derecha.getY()):
                        gasD=CmGas.obtener(int(CAx),int(CAy)).derecha.getDato()
                        disD=abs(int(CPfx)-CmGas.obtener(int(CAx),int(CAy)).derecha.getX())+abs(int(CPfy)-CmGas.obtener(int(CAx),int(CAy)).derecha.getY())
                        futD=op2.EvaluarFuturo(ListaCC,CmGas,CmGas.obtener(int(CAx),int(CAy)).derecha.getX(),CmGas.obtener(int(CAx),int(CAy)).derecha.getY(),CPfx,CPfy)
                        derecha=gasD+disD+futD
                    else:
                        derecha=999
                except:
                    derecha=999

                y=CAy
                x=CAx
                if disA==1 or disA==0:
                    print("Avanzando hacia arriba ("+str(CmGas.obtener(int(x),int(y)).arriba.getX())+" , "+str(CmGas.obtener(int(x),int(y)).arriba.getY())+")\n")
                    CAx=CmGas.obtener(int(x),int(y)).arriba.getX()
                    CAy=CmGas.obtener(int(x),int(y)).arriba.getY()
                    continue
                    
                if disAb==1 or disAb==0:
                    print("Avanzando hacia abajo ("+str(CmGas.obtener(int(x),int(y)).abajo.getX())+" , "+str(CmGas.obtener(int(x),int(y)).abajo.getY())+")\n")
                    CAx=CmGas.obtener(int(x),int(y)).abajo.getX()
                    CAy=CmGas.obtener(int(x),int(y)).abajo.getY()
                    continue

                if disD==1 or disD==0:
                    print("Avanzando hacia la derecha ("+str(CmGas.obtener(int(x),int(y)).derecha.getX())+" , "+str(CmGas.obtener(int(x),int(y)).derecha.getY())+")\n")
                    CAx=CmGas.obtener(int(x),int(y)).derecha.getX()
                    CAy=CmGas.obtener(int(x),int(y)).derecha.getY()
                    continue

                if disI==1 or disI==0:
                    print("Avanzando hacia la derecha ("+str(CmGas.obtener(int(x),int(y)).izquierda.getX())+" , "+str(CmGas.obtener(int(x),int(y)).izquierda.getY())+")\n")
                    CAx=CmGas.obtener(int(x),int(y)).izquierda.getX()
                    CAy=CmGas.obtener(int(x),int(y)).izquierda.getY()
                    continue

                if arriba<=abajo and arriba<=izquierda and arriba<=derecha:
                    print("Avanzando hacia arriba ("+str(CmGas.obtener(int(x),int(y)).arriba.getX())+" , "+str(CmGas.obtener(int(x),int(y)).arriba.getY())+")\n")
                    CAx=CmGas.obtener(int(x),int(y)).arriba.getX()
                    CAy=CmGas.obtener(int(x),int(y)).arriba.getY()
                    continue
                    
                if abajo<=arriba and abajo<=izquierda and abajo<=derecha:
                    print("Avanzando hacia abajo ("+str(CmGas.obtener(int(x),int(y)).abajo.getX())+" , "+str(CmGas.obtener(int(x),int(y)).abajo.getY())+")\n")
                    CAx=CmGas.obtener(int(x),int(y)).abajo.getX()
                    CAy=CmGas.obtener(int(x),int(y)).abajo.getY()
                    continue

                if derecha<=abajo and derecha<=izquierda and derecha<=arriba:
                    print("Avanzando hacia la derecha ("+str(CmGas.obtener(int(x),int(y)).derecha.getX())+" , "+str(CmGas.obtener(int(x),int(y)).derecha.getY())+")\n")
                    CAx=CmGas.obtener(int(x),int(y)).derecha.getX()
                    CAy=CmGas.obtener(int(x),int(y)).derecha.getY()
                    continue

                if izquierda<=abajo and izquierda<=arriba and izquierda<=derecha:
                    print("Avanzando hacia la derecha ("+str(CmGas.obtener(int(x),int(y)).izquierda.getX())+" , "+str(CmGas.obtener(int(x),int(y)).izquierda.getY())+")\n")
                    CAx=CmGas.obtener(int(x),int(y)).izquierda.getX()
                    CAy=CmGas.obtener(int(x),int(y)).izquierda.getY()
                    continue

            Gasolina+=CmGas.obtener(int(CAx),int(CAy)).getDato()
            ListaCC.insertar(ListaCerrada(int(CAx),int(CAy)))
            print("Se ha llegado al destino")
            print("Gasolina utilizada: "+str(Gasolina))
                    
            print("\n")  

            for j in range(int(DimF)):
                for i in range(int(DimC)):
                    if ListaCC.ExisteCoordenada(CmGas.obtener(int(i),int(j)).getX(),CmGas.obtener(int(i),int(j)).getY()):
                        print(0,end=" ")   
                    else:
                        print(1,end=" ")     
                print() 

            print("\n\n")
            
            #Verificando si existe el terreno
            sn=ListaRR.bus(NomT)
             
            #Guardando terreno
            if sn:
                ListaRR.insertar(Resultado(NomT,CPix+1,CPiy+1,CPfx+1,CPfy+1,DimC,DimF,Gasolina,ListaCC))
            ListaRR.mostrar()
        return ListaRR
                    
                    

                





    def EvaluarFuturo(ListaCC,CmGas,CAx,CAy,CPfx,CPfy):
        #Arriba
        try:
            if ListaCC.ExisteCoordenada(CmGas.obtener(int(CAx),int(CAy)).arriba.getX(),CmGas.obtener(int(CAx),int(CAy)).arriba.getY()):
                gasA=CmGas.obtener(int(CAx),int(CAy)).arriba.getDato()
                disA=abs(int(CPfx)-CmGas.obtener(int(CAx),int(CAy)).arriba.getX())+abs(int(CPfy)-CmGas.obtener(int(CAx),int(CAy)).arriba.getY())
                arriba=gasA+disA
            else:
                arriba=999
        except:
            arriba=999
        #Abajo
        try:
            if ListaCC.ExisteCoordenada(CmGas.obtener(int(CAx),int(CAy)).abajo.getX(),CmGas.obtener(int(CAx),int(CAy)).abajo.getY()):
                gasAb=CmGas.obtener(int(CAx),int(CAy)).abajo.getDato()
                disAb=abs(int(CPfx)-CmGas.obtener(int(CAx),int(CAy)).abajo.getX())+abs(int(CPfy)-CmGas.obtener(int(CAx),int(CAy)).abajo.getY())
                abajo=gasAb+disAb
            else:
                abajo=999
        except:
            abajo=999
        #Izquierda
        try:
            if ListaCC.ExisteCoordenada(CmGas.obtener(int(CAx),int(CAy)).izquierda.getX(),CmGas.obtener(int(CAx),int(CAy)).izquierda.getY()):
                gasI=CmGas.obtener(int(CAx),int(CAy)).izquierda.getDato()
                disI=abs(int(CPfy)-CmGas.obtener(int(CAx),int(CAy)).izquierda.getY())+abs(int(CPfx)-CmGas.obtener(int(CAx),int(CAy)).izquierda.getX())
                izquierda=gasI+disI
            else:
                izquierda=999
        except:
            izquierda=999
        #Derecha
        try:
            if ListaCC.ExisteCoordenada(CmGas.obtener(int(CAx),int(CAy)).derecha.getX(),CmGas.obtener(int(CAx),int(CAy)).derecha.getY()):
                gasD=CmGas.obtener(int(CAx),int(CAy)).derecha.getDato()
                disD=abs(int(CPfx)-CmGas.obtener(int(CAx),int(CAy)).derecha.getX())+abs(int(CPfy)-CmGas.obtener(int(CAx),int(CAy)).derecha.getY())
                derecha=gasD+disD
            else:
                derecha=999
        except:
            derecha=999

        rut=0


        if arriba<=abajo and arriba<=izquierda and arriba<=derecha:
            rut=arriba
            
        if abajo<=arriba and abajo<=izquierda and abajo<=derecha:
            rut=abajo
            
        if izquierda<=abajo and izquierda<=arriba and izquierda<=derecha:
            rut=izquierda
            
        if derecha<=abajo and derecha<=izquierda and derecha<=arriba:
            rut=derecha

        return rut
            
                


                
                
                







