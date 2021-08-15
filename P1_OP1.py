import xml.etree.ElementTree as ET
from tkinter import filedialog as FileDialog
from ObjTerreno import Terreno
from ObjTerreno import Lista
from MOrto import MOrto
from NOrtogonal import NodoOrtogonal

Terrenos=Lista()
gass=MOrto()

class op1:
    def CargarArchivo():
        print("\n\n")
        print("******************* Cargar Archivo *******************")
        ruta=input("Ingrese la ruta del archivo\n")
        
        archivo=ET.parse(ruta)
        raiz = archivo.getroot()
        
        for terrenos in raiz.findall('terreno'):
            gass=MOrto()
            #obteniendo nombre del terreno
            nombre=terrenos.get('nombre')
            #Obteniendo posicion de inicio
            for dimension in terrenos.findall('dimension'):
                #Tamaño en x
                for xy in dimension.findall('m'):
                    m=xy.text
                #Tamaño en y
                for xy in dimension.findall('n'):
                    n=xy.text
            for coordenadas in terrenos.findall('posicioninicio'):
                #Coordenada en x
                for xy in coordenadas.findall('x'):
                    pix=xy.text
                #Coordenada en y
                for xy in coordenadas.findall('y'):
                    piy=xy.text
                
            #Obteniendo posicion final
            for coordenadas in terrenos.findall('posicionfin'):
                #Coordenada en x
                for xy in coordenadas.findall('x'):
                    pfx=xy.text
                #Coordenada en y
                for xy in coordenadas.findall('y'):
                    pfy=xy.text
                
            #Coordenadas Matriz
            #gas=None
            for coordenadas in terrenos.findall('posicion'):
                #Coordenada en x
                px=coordenadas.get('x')
                #Coordenada en y
                py=coordenadas.get('y')
                #Gasolina por celda
                gaso=coordenadas.text
                gas=gass.insertar(NodoOrtogonal(int(gaso),int(py)-1,int(px)-1))
            #print(gas)
            sn=True

#********************************************************************************************************************
            gass.recorrer()
            print("*******************")
            
            #Verificando si existe el terreno
            sn=Terrenos.bus(nombre)
             
            #Guardando terreno
            if sn:
                Terrenos.insertar(Terreno(nombre,pix,piy,pfx,pfy,gass,m,n))
            
            #gass.recorrer.getDato()

#********************************************************************************************************************
            
        #retornando una lista con los parámetros obtenidos
        #Terrenos.mostrar()
        return Terrenos
        