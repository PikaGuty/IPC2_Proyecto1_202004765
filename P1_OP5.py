import subprocess

class op5:
    def GenerarGrafica(Terrenos,Result):
        Res=Result
        Terr=Terrenos
        cc=Res.longitud()
        seleccion = 0
        while seleccion != (cc+1):
            cc=Res.longitud()
            print("\n\n\n")
            print('***************************************************************\n'+
                '**       SELECCIONE EL TERRENO PARA GENERAR SU GRÁFICA       **\n'+
                '***************************************************************')
            Res.mostrarM()
            print("**  {:<4}{:<51}  **".format((str(cc+1)+"."),"Regresar al menú principal"))    
            print('***************************************************************')
            try:
                seleccion = int(input())
            except:
                print("Debe ingresar un número")
            if seleccion==(cc+1):
                break
            elif seleccion>(cc+1):
                print("Seleccione un numero del menú")
                continue
            try:
                Ress = Res.retornar_seleccionado(seleccion)
            except:
                break

            NomT=Terr.retornar(Ress.getNombre()).getNombre()
            #Dimension de Columnas
            DimC=Terr.retornar(Ress.getNombre()).getDimc()
            #Dimension de Filas
            DimF=Terr.retornar(Ress.getNombre()).getDimf()
            #Matriz ortogonal de gas y coordenadas
            CmGas=Terr.retornar(Ress.getNombre()).getGas()
            tabla=""
            for j in range(int(DimC)):
                tabla+='<TR>'
                for i in range(int(DimF)):
                    if Ress.getRecorrido().ExisteCoordenada(int(i),int(j)):
                        gas=CmGas.obtener(i,j).getDato()
                        tabla+='<TD border="3"  bgcolor="lightgoldenrod1" gradientangle="315">'+str(gas)+'</TD>'   
                    else:
                        gas=CmGas.obtener(i,j).getDato()
                        tabla+='<TD border="3"  bgcolor="goldenrod" gradientangle="315">'+str(gas)+'</TD>'
                tabla+='</TR>' 
                print()

            encabezado='digraph G { bgcolor="goldenrod3" style="filled"'+'node [shape=record]'+'a0 [label=<'+'<TABLE border="10" cellspacing="10" cellpadding="10" style="rounded" bgcolor="grey86" gradientangle="315">'

                  
            final='</TABLE>>];'+'}'

            #bin\dot.exe -Tpng eje.txt -o le.png
            try:
                f = open (str(NomT).replace(" ","")+'.txt','w')
                contenido=encabezado+tabla+final
                
                f.write(contenido)
                f.close()
                subprocess.run('bin\dot.exe -Tpng '+str(NomT).replace(" ","")+'.txt -o '+str(NomT).replace(" ","")+'.png')
                print("Imagen generada")
            except:
                print("Ha ocurrido un error, intentelo nuevamente")

            

