import xml.etree.ElementTree as ET
from tkinter import filedialog as FileDialog

class op1:
    def CargarArchivo():
        
        #print("******************* Cargar Archivo *******************")
        #ruta=input("Ingrese la ruta del archivo\n")
        
        archivo=ET.parse('C:/Users/gohan/OneDrive - Facultad de Ingeniería de la Universidad de San Carlos de Guatemala/U/4 to Semestre/Laboratorio IPC2/IPC2_Proyecto1_202004765/prueba.xml')

        raiz = archivo.getroot()
        
        for terrenos in raiz:
            print(terrenos.attrib)
            for coordenadas in terrenos:
                for xy in coordenadas:
                    print("Posición I/F"+xy.text)
                print(coordenadas)
                print(coordenadas.attrib)


        #print("Archivo analizado con éxito")
        #retornando una lista con los parámetros obtenidos
        