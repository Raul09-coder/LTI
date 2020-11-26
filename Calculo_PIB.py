import os

Clean = lambda: os.system('cls')

mtzPIB = []
dicPIB = dict(Enfoque = "",PIB = 0)
IN = None

while True:
    Clean()
    print("== Calculador de PIB ==\nBienvenido al sistema")
    print("1.-Calcular PIB")
    print("2.-Reporte de PIB Calculados")
    print("\n0.-Salir\n")
    Opcion = input("Selecciona una opción: ")

    if Opcion == "":
        print("ERROR: Por favor seleccione una opción")
        input("Presiona ENTER para continuar...")
        Clean()
    elif Opcion == "1":
        while True:
            Clean()
            print("== CALCULADOR DE PIB ==")
            print("1.-Enfoque del Gasto")
            print("2.-Enfoque del Ingreso")
            print("\n0.-Regresar\n")
            OpcionPIB = input("Selecciona una opción a realizar: ")

            if str(OpcionPIB) == "":
                print("ERROR: Por favor seleccione una opción")
                input("Presiona ENTER para continuar...")
                Clean()
            elif OpcionPIB == "1":
                ##Enfoque del Gasto
                Clean()
                print("== ENFOQUE DE GASTOS ==")
                C = float(input("Ingresa el Gasto de Consumo Personal o Familiar: "))
                Ig = float(input("Ingresa la Inversión Dómestica Privada Bruta: "))
                G = float(input("Ingresa las Compras o Gasto del Gobierno: "))
                Xn = float(input("Ingresa las Exportaciones Netas: "))
                print()
                print(f"Calculador del PIB = {C} + {Ig} + {G} + {Xn}\n")
                PIB = C+Ig+G+Xn
                print("PIB = ",PIB)
                dicPIB["Enfoque"] = "GASTO"
                dicPIB["PIB"] = PIB
                input("Presiona ENTER para continuar...")
                mtzPIB.append(dicPIB.copy())
                Clean()

            elif OpcionPIB == "2":
                ##Enfoque de Ingreso
                Clean()
                print("== ENFOQUE DE INGRESOS ==")
                print("1.-Calcular Ingreso Nacional")
                print("2.-Calcular PIB")
                print("\n0.-Regresar\n")

                OpcionIN = input("Selecciona una opción: ")

                if str(OpcionIN) == "":
                    print("ERROR: Por favor seleccione una opción")
                    input("Presiona ENTER para continuar...")
                    Clean()
                elif OpcionIN == "1":
                    ##Calcular IN
                    Rt = float(input("Ingresa las Remuneraciones de los trabajadores(ej. Sueldos y salarios): "))
                    R = float(input("Ingresa las Rentas: "))
                    In = float(input("Ingresa los Intereses (ej. Pago de depositos de ahorro): "))
                    Ip = float(input("Ingrese los Ingresos de los propietarios (ingreso neto de empresas propias): "))
                    Bc = float(input("Ingrese los Beneficios corporativos: "))

                    print(f"Ingreso Nacional = {Rt} + {R} + {In} + {Ip} + {Bc}")
                    IN = Rt + R + In + Ip + Bc
                    print("Ingreso Nacional = ",IN)
                    input("Presiona ENTER para continuar...")
                    Clean()

                elif OpcionIN == "2":
                    ##Calcular PIB Ingresos
                    if IN == None:
                        IN = float(input("Ingresa el valor del Ingreso Nacional: "))
                    else:
                        pass
                    IIE = float(input("Ingresa los Impuestos Indirectos a las Empresas (ej. IVA):"))
                    dep = float(input("Ingresa el Consumo de Capital Fijo (Depreciación): "))
                    INFE = float(input("Ingresa el Ingreso Neto de los Factores Extranjeros: "))
                    print(f"Calulador de PIB = {IN} + {IIE} + {dep} + {INFE}")
                    PIB = IN + IIE + dep + INFE
                    print("PIB = ",PIB)
                    dicPIB["Enfoque"] = "Ingreso"
                    dicPIB["PIB"] = PIB
                    input("Presiona ENTER para continuar...")
                    mtzPIB.append(dicPIB.copy())
                    Clean()

                else:
                    print("ERROR: Valor ingresado no valido...")
                    input("Presiona ENTER para continuar...")
                    Clean()
            elif OpcionPIB == "0":
                break
            else:
                print("ERROR: Valor ingresado no valido...")
                input("Presiona ENTER para continuar...")
                Clean()
        

    elif Opcion == "2":
        print("== REPORTE DE PIB ==")
        for reporte in mtzPIB:
            print(reporte)
        input("Presiona ENTER para continuar")
        Clean()
    elif Opcion == "0":
        print("Saliendo del sistema...")
        break
    else:
        print("ERROR: Valor ingresado no valido...")
        input("Presiona ENTER para continuar...")
        Clean()
