import xml.etree.ElementTree as ET
from tkinter import filedialog as FileDialog
from ObjTerreno import Terreno

Terrenos=[]

class op1:
    def CargarArchivo():
        
        #print("******************* Cargar Archivo *******************")
        #ruta=input("Ingrese la ruta del archivo\n")
        
        archivo=ET.parse('C:/Users/gohan/OneDrive - Facultad de Ingeniería de la Universidad de San Carlos de Guatemala/U/4 to Semestre/Laboratorio IPC2/IPC2_Proyecto1_202004765/prueba.xml')
        raiz = archivo.getroot()
        
        for terrenos in raiz.findall('terreno'):
            #obteniendo nombre del terreno
            nombre=terrenos.get('nombre')
            #print(nombre)
            #Obteniendo posicion de inicio
            for coordenadas in terrenos.findall('posicioninicio'):
                #Coordenada en x
                for xy in coordenadas.findall('x'):
                    pix=xy.text
                #Coordenada en y
                for xy in coordenadas.findall('y'):
                    piy=xy.text
                inicio=[int(pix),int(piy)]
                #print(inicio)
            #Obteniendo posicion final
            for coordenadas in terrenos.findall('posicionfin'):
                #Coordenada en x
                for xy in coordenadas.findall('x'):
                    pfx=xy.text
                #Coordenada en y
                for xy in coordenadas.findall('y'):
                    pfy=xy.text
                fin=[int(pfx),int(pfy)]
                #print(fin)
            #Coordenadas Matriz
            gas={}
            for coordenadas in terrenos.findall('posicion'):
                #Coordenada en x
                px=coordenadas.get('x')
                #Coordenada en y
                py=coordenadas.get('y')
                #Gasolina por celda
                gaso=coordenadas.text
                gass={""+str(px)+","+str(py):int(gaso)}
                gas.update(gass)
            #print(gas)
            sn=True
            #Verificando si existe el terreno
            for t in Terrenos:
                if nombre==t.getNombre():
                    sn=False
                    #print("El terreno "+nombre+" ya existe")
            #Guardando terreno
            if sn:
                NewT=Terreno(nombre,inicio,fin,gas)
                Terrenos.append(NewT)
            
            
        #retornando una lista con los parámetros obtenidos
        return Terrenos
        