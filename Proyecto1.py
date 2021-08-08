from P1_OP1 import op1
from P1_OP2 import op2
from P1_OP3 import op3
from P1_OP4 import op4
from P1_OP5 import op5
from P1_OP6 import op6
from ObjTerreno import Terreno

seleccion = 0
res=[]

while seleccion != 6:
    print('***************************************************************\n'+
          '**                            MENU                           **\n'+
          '***************************************************************\n'+
          '** 1. Cargar archivo                                         **\n'+
          '** 2. Procesar archivo                                       **\n'+
          '** 3. Escribir archivo salida                                **\n'+
          '** 4. Mostrar datos del estudiante                           **\n'+
          '** 5. Generar gráfica                                        **\n'+
          '** 6. Salir                                                  **\n'+
          '***************************************************************')
    print('Seleccione una opción del menú')
    try:
        seleccion = int(input())
    except:
        print("Debe ingresar un número")
    if seleccion==1:
        Terrenos=op1.CargarArchivo()
    elif seleccion==2:
        op2.ProcesarTerreno(Terrenos)
    elif seleccion==3:
        op3.EscribirArchivo()
    elif seleccion==4:
        op4.MostrarDatosE()
    elif seleccion==5:
        op5.GenerarGrafica()
    elif seleccion==6:
        print("¿Quiere salir? S/N")
        conf=input().upper()
        if conf=="S":
            op6.Despedirse()
        elif conf=="N":
            seleccion=0
        else:
            print("Debe ingresar una opción del menú")
    elif seleccion==0:
        print("")
    else:
        print("Escoja un número del menú")
