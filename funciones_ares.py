import csv
import utilidades

def buscar_pais():
    pais_buscar = input("Nombre del país a buscar: ")
    pais_buscar = pais_buscar.strip()
    pais_buscar = pais_buscar.lower()
    pais_buscar = utilidades.normalizar_caracteres(pais_buscar)

    pais_encontrado = False
    print()

    with open("paises.csv", "r", newline='') as archivo:
        lector = csv.reader(archivo)
        next(lector)
        for fila in lector:
            if fila:
                if (fila[0]).lower() == pais_buscar:
                    pais_encontrado = True
                    print(fila[0])
                    print(f"Población: {fila[1]}")
                    print(f"Superficie: {fila[2]} km^2\n")
                elif pais_buscar in (fila[0]).lower():
                    pais_encontrado = True
                    print(fila[0])
                    print(f"Población: {fila[1]}")
                    print(f"Superficie: {fila[2]} km^2\n")

    if not pais_encontrado:
        print("País no encontrado.\n")                    

def filtrar_por_continente():
    continente_filtrar = input("Nombre del continente a filtrar: ")
    continente_filtrar = continente_filtrar.strip()
    continente_filtrar = continente_filtrar.capitalize()
    print()
    
    continente_encontrado = False

    with open("paises.csv", "r", newline='') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            if fila and fila[3] == continente_filtrar:
                continente_encontrado = True
                print(fila[0])
                print(f"Población: {fila[1]}")
                print(f"Superficie: {fila[2]} km^2\n")

    if not continente_encontrado:
        print("Continente no encontrado.\n")

def filtrar_rango_poblacion():
    while True:
        try:
            print("Filtrando por población:")
            limite_inferior = int(input("Ingrese el límite inferior del rango: "))
            limite_superior = int(input("Ingrese el límite superior del rango: "))

            if limite_inferior < 0 or limite_superior < 0:
                print("Inválido - los límites no pueden ser menores a 0.\n")
            elif limite_superior < limite_inferior:
                print("Inválido - el límite superior no puede ser menor al límite inferior.\n")
        except ValueError:
            print("Inválido - los valores deben ser un número entero.\n")
        else:
            break

    pais_encontrado = False
    print()

    with open("paises.csv", "r", newline='') as archivo:
        lector = csv.reader(archivo)
        next(lector)
        for fila in lector:
            if fila:
                if limite_superior > int(fila[1]) > limite_inferior:
                    pais_encontrado = True
                    print(fila[0])
                    print(f"Población: {fila[1]}")
                    print(f"Superficie: {fila[2]} km^2\n") 

    if not pais_encontrado:
        print("No se encontró ningún país dentro del rango.\n")

def filtrar_rango_superficie():
    while True:
        try:
            print("Filtrando por superficie:")
            limite_inferior = float(input("Ingrese el límite inferior del rango: "))
            limite_superior = float(input("Ingrese el límite superior del rango: "))

            if limite_inferior < 0 or limite_superior < 0:
                print("Inválido - los límites no pueden ser menores a 0.\n")
            elif limite_superior < limite_inferior:
                print("Inválido - el límite superior no puede ser menor al límite inferior.\n")
        except ValueError:
            print("Inválido - los valores deben ser un número entero o decimal.\n")
        else:
            break

    pais_encontrado = False
    print()

    with open("paises.csv", "r", newline='') as archivo:
        lector = csv.reader(archivo)
        next(lector)
        for fila in lector:
            if fila:
                if limite_superior > int(fila[2]) > limite_inferior:
                    pais_encontrado = True
                    print(fila[0])
                    print(f"Población: {fila[1]}")
                    print(f"Superficie: {fila[2]} km^2\n") 

    if not pais_encontrado:
        print("No se encontró ningún país dentro del rango.\n")

def menu_filtrar_paises():
    print("===MENÚ===")
    print("Filtrar por:")
    print("    |1| Continente")
    print("    |2| Rango de población")
    print("    |3| Rango de superficie")
    print("    |4| Salir\n")

    while True:
        opt = input("Opción: ")
        print()

        if opt == '1':
            filtrar_por_continente()
        elif opt == '2':
            filtrar_rango_poblacion()
        elif opt == '3':
            filtrar_rango_superficie()
        elif opt == '4':
            break
        else:
            print("Opción inválida")