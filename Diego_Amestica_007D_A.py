import random
import csv
from statistics import geometric_mean
planilla_empleados = []


def asignar_sueldos_aleatorios():
    while True:
        cantidad = 10
        numero = 0
        for i in range(cantidad):
            numero +=1
            print()
            nombre_trabajador = input(f"Ingrese el nombre del trabajador {numero}\n==> ")
            longitud_nombre = len(nombre_trabajador)
            print()
            apellido_trabajador = input(f"Ingrese el apellido del trabajador {numero}\n==> ")
            longitud_apellido = len(apellido_trabajador)
            print()
            while nombre_trabajador.isalpha() == False or longitud_nombre<3 or apellido_trabajador.isalpha() == False or longitud_apellido<3:
                print()
                print("[ERROR] [EL NOMBRE Y APELLIDO DEBEN CONTENER LETRAS] [NO DEBEN SER MENOR A 3 CARACTERES]")
                print()
                nombre_trabajador = input("Ingrese el nombre del trabajador\n==> ")
                longitud_nombre = len(nombre_trabajador)
                print()
                apellido_trabajador = input("Ingrese el apellido del trabajador\n==> ")
                longitud_apellido = len(apellido_trabajador)
                print()
            sueldo_trabajador = random.randint(300000,2500000)
            diccionario_trabajador = {
                "Nombre": nombre_trabajador +  apellido_trabajador,
                "Sueldo": sueldo_trabajador, 
                "Descuento salud": (round(sueldo_trabajador*0.07)),
                "Descuento AFP": (round(sueldo_trabajador*0.12)),
                "Sueldo liquido": (round(sueldo_trabajador*0.81))
            }
            planilla_empleados.append(diccionario_trabajador)
        print("[INFORMACION DE EMPLEADOS INGRESADA CON EXITO]")
        break

def clasificar_sueldos():
    if not planilla_empleados:
        print("[LA PLANILLA DE EMPLEADOS ESTÁ VACIA]")
    for diccionario_trabajador in planilla_empleados:
        if diccionario_trabajador["Sueldo"]<800000:
            cantidad_menor = 0 
            cantidad_menor = cantidad_menor + 1
            while diccionario_trabajador["Sueldo"]<800000:
                if diccionario_trabajador["Sueldo"]<800000 == None:
                    print(f"Sueldos menores a $800.000\t Total {0} ")
                    break
                else:
                    print(f"Sueldos menores a $800.000\t Total {cantidad_menor} ")
                    print(diccionario_trabajador)
                    print()
                    break
    for diccionario_trabajador in planilla_empleados:
        if diccionario_trabajador["Sueldo"]>800000 or diccionario_trabajador["Sueldo"]<2000000:
            cantidad_media = 0 
            cantidad_media = cantidad_media + 1
            while diccionario_trabajador["Sueldo"]>800000 or diccionario_trabajador["Sueldo"]<2000000:
                if diccionario_trabajador["Sueldo"]>800000 or diccionario_trabajador["Sueldo"]<2000000 == None:
                    print(f"Sueldos entre $800.000 y $2.000.000\t Total {0} ")
                    break
                else:
                    print(f"Sueldos entre $800.000 y $2.000.000\t Total {cantidad_media}")
                    print(diccionario_trabajador)
                    print()
                    break

    for diccionario_trabajador in planilla_empleados:
        if diccionario_trabajador["Sueldo"]>2000000:
            cantidad_mayor = 0 
            cantidad_mayor = cantidad_mayor + 1
            while diccionario_trabajador["Sueldo"]>2000000:
                if diccionario_trabajador["Sueldo"]<2000000 == None:
                    print(f"Sueldos superiores a $2.000.000\t Total {0} ")
                    break
                else:
                    print(f"Sueldos superiores a $2.000.000\t Total {cantidad_mayor}")
                    print(diccionario_trabajador)
                    print()
                    break

def ver_estadistica():
    if not planilla_empleados:
        print("[LA PLANILLA DE EMPLEADOS ESTÁ VACIA]")
    else:
        while True:
            try:
                print()
                opciones = int(input("INFORMACION DE SUELDOS\n1. Sueldo más alto\n2. Sueldo más bajo\n3. Promedio de sueldos\n4. Media geometrica\n5. Retroceder\n==> "))
                print()
                while opciones<1 or opciones>5:
                    print()
                    print("[ERROR] [PARA OBTENER INFORMACION SOBRE LOS SUELDOS DEBE INGRESAR 1, 2, 3, 4 o 5]")
                    print( )
                    opciones = int(input("INFORMACION DE SUELDOS\n1. Sueldo más alto\n2. Sueldo más bajo\n3. Promedio de sueldos\n4. Media geometrica\n5. Retroceder\n==> "))
                    print()
            except ValueError:
                print()
                print("[ERROR] [DEBE INGRESAR UN VALOR NUMERICO]")
                print()
                continue
            for diccionario_trabajador in planilla_empleados:  
                if opciones==1:
                    if diccionario_trabajador["Sueldo"]>2000000:
                        print(diccionario_trabajador)
                    elif diccionario_trabajador["Sueldo"]<2000000 and diccionario_trabajador["Sueldo"]>800000:
                        print(diccionario_trabajador)
                    elif diccionario_trabajador["Sueldo"]<800000:
                        print(diccionario_trabajador)
                elif opciones==2:
                    if diccionario_trabajador["Sueldo"]<800000:
                            print(diccionario_trabajador)
                    elif diccionario_trabajador["Sueldo"]<2000000 and diccionario_trabajador["Sueldo"]>800000:
                            print(diccionario_trabajador)
                    elif diccionario_trabajador["Sueldo"]>2000000:
                                print(diccionario_trabajador)
                elif opciones==3:
                    promedio = (sum(diccionario_trabajador["Sueldo"])/10)
                    print(promedio)
                    print()
                elif opciones==4:
                    print()
                elif opciones==5:
                    return
            


def reporte_de_sueldos():
    with open("reporte_de_sueldos.csv", "w", newline="") as archivo_csv: 
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow(["Nombre", "Sueldo base", "Descuento salud", "Descuento AFP", "Sueldo liquido"])
        for diccionario_trabajador in planilla_empleados:
            escritor_csv.writerow([diccionario_trabajador["Nombre"], diccionario_trabajador["Sueldo"], diccionario_trabajador["Descuento salud"], diccionario_trabajador["Descuento AFP"], diccionario_trabajador["Sueldo liquido"]])
    print("[ARCHIVO CSV GENERADO CON EXITO]")


def programa_principal():
    while True:
        from os import system
        system("cls")
        try:
            print()
            opciones = int(input("[MENU EMPRESA]\n1. Asignar sueldos aleatorios\n2. Clasificar sueldos\n3. Ver estadisticas\n4. Reporte de sueldos\n5. Salir del programa\n==> "))
            print()
            while opciones<1 or opciones>5:
                print()
                print("[ERROR] [LA SELECCION DEL MENU DEBE SER ENTRE 1, 2, 3, 4 o 5]")
                print()
                opciones = int(input("[MENU EMPRESA]\n1. Asignar sueldos aleatorios\n2. Clasificar sueldos\n3. Ver estadisticas\n4. Reporte de sueldos\n5. Salir del programa\n==> "))
                print()
        except ValueError:
            print()
            print("[ERROR] [DEBE INGRESAR UN VALOR NUMERICO]")
            print()
            input("Ingrese una tecla para continuar\n==> ")       
            continue
        if opciones==1:
            asignar_sueldos_aleatorios()
        elif opciones==2:
            clasificar_sueldos()
        elif opciones==3:
            ver_estadistica()
        elif opciones==4:
            reporte_de_sueldos()
        elif opciones==5:
            break         
        input("Ingrese una tecla para continuar\n==> ")       

programa_principal()