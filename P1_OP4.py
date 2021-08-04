class op4:
    def MostrarDatosE():
        seleccion=0
        while seleccion != "":
            print("\n\n\n"+
                "*****************************************************************\n"+
                "** > Javier Alejandro Gutierrez de León                        **\n"+
                "** > 202004765                                                 **\n"+
                "** > Introducción a la Programación y Computación 2 sección A  **\n"+
                "** > Ingeniería en Ciencias y Sistemas                         **\n"+
                "** > 4to Semestre                                              **\n"+
                "*****************************************************************\n\n\n"+
                "Presione enter para regresar al menú principal")
            
            seleccion = input()
            
            if seleccion=="":
                print("Regresando al menú principal ...\n")
            else:
                print("Debe presionar enter\n")