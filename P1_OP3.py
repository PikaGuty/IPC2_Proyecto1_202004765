import xml.etree.cElementTree as ET
import xml.dom.minidom
from xml.dom import minidom
from resultado import Resultado
from resultado import ListaR

class op3:
    def EscribirArchivo(Result):
        Res=Result
        cc=Res.longitud()
        seleccion = 0
        while seleccion != (cc+1):
            cc=Res.longitud()
            print("\n\n\n")
            print('***************************************************************\n'+
                '**  SELECCIONE EL TERRENO PARA GENERAR SU ARCHIVO DE SALIDA  **\n'+
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
        #******************************************************************
            root = ET.Element("terrenos")
            doc = ET.SubElement(root, "terreno", name=str(Ress.getNombre()))

            a=ET.SubElement(doc, "dimension")
            ET.SubElement(a, "m").text=str(Ress.getDimc())
            ET.SubElement(a, "n").text=str(Ress.getDimf())

            b=ET.SubElement(doc, "posicioninicio")
            ET.SubElement(b, "x").text=str(Ress.getPiy())
            ET.SubElement(b, "y").text=str(Ress.getPix())

            c=ET.SubElement(doc, "posicionfin")
            ET.SubElement(c, "x").text=str(Ress.getPfy())
            ET.SubElement(c, "y").text=str(Ress.getPfx())

            ET.SubElement(doc, "combustible").text = str(Ress.getGas())

            recor=Ress.getRecorrido()
            for j in range(int(Ress.getDimc())):
                for i in range(int(Ress.getDimf())):
                    if not recor.ExisteCoordenada(i,j):
                        ET.SubElement(doc, "posicion", y=str(j),x=str(i)).text = "1"
                print() 

            print("\n\n")
            

            xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ")
            with open(str(Ress.getNombre())+".xml", "w") as f:
                f.write(xmlstr)
