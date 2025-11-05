import csv
import utilidades # Modulo local con funciones auxiliares (ej. normalizar)

def buscar_pais():
    # Solicita y normaliza el termino de busqueda del usuario
    pais_buscar = input("Nombre del país a buscar: ")
    pais_buscar = pais_buscar.strip() # Quita espacios en blanco
    pais_buscar = pais_buscar.lower() # Convierte a minusculas
    pais_buscar = utilidades.normalizar_caracteres(pais_buscar) # Quita tildes

    pais_encontrado = False
    print()

    # Abre el archivo CSV para lectura
    with open("paises.csv", "r", newline="", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        next(lector) # Omite la fila de encabezado
        for fila in lector:
            if fila: # Asegura que la fila no este vacia
                # Comprueba coincidencia exacta (normalizada)
                if (fila[0]).lower() == pais_buscar:
                    pais_encontrado = True
                    print(fila[0])
                    print(f"Población: {int(fila[1]):,}")
                    print(f"Superficie: {float(fila[2]):,.0f} km^2\n")
                # Comprueba coincidencia parcial (si el termino esta contenido)
                elif ((fila[0]).lower()).startswith(pais_buscar):
                    pais_encontrado = True
                    print(fila[0])
                    print(f"Población: {int(fila[1]):,}")
                    print(f"Superficie: {float(fila[2]):,.0f} km^2\n")

    if not pais_encontrado:
        print("País no encontrado.")                    

def filtrar_por_continente():
    continente_filtrar = input("\nNombre del continente a filtrar: ")
    continente_filtrar = utilidades.normalizar_caracteres(continente_filtrar)
    continente_filtrar = continente_filtrar.strip().capitalize()
    print()

    # Lista de continentes válidos (normalizados)
    continentes_validos = ["America", "Europa", "Asia", "Africa", "Oceania"]

    # Validación
    if continente_filtrar not in continentes_validos:
        print("Continente inválido.\n")
        return

    continente_encontrado = False

    with open("paises.csv", "r", newline="", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        next(lector)  # Omitir encabezado

        for fila in lector:
            if fila:
                # Normalizar el continente del CSV
                continente_csv = utilidades.normalizar_caracteres(fila[3]).capitalize()

                # Comparación ya normalizada
                if continente_csv == continente_filtrar:
                    continente_encontrado = True
                    print(fila[0])
                    print(f"Población: {int(fila[1]):,}")
                    print(f"Superficie: {float(fila[2]):,.0f} km^2\n")

    if not continente_encontrado:
        print("No se encontraron países en ese continente.\n")


def filtrar_rango_poblacion():
    print("Filtrando por población:")

    # Validación del rango
    try:
        limite_inferior = int(input("Ingrese el límite inferior del rango: "))
        limite_superior = int(input("Ingrese el límite superior del rango: "))

        if limite_inferior < 0 or limite_superior < 0:
            print("Inválido - los límites no pueden ser menores a 0.\n")
            return   

        if limite_superior < limite_inferior:
            print("Inválido - el límite superior no puede ser menor al límite inferior.\n")
            return   

    except ValueError:
        print("Inválido - los valores deben ser un número entero.\n")
        return   

    pais_encontrado = False
    print()

    with open("paises.csv", "r", newline="", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        next(lector)  # Salta encabezado
        for fila in lector:
            if fila:
                poblacion = int(fila[1])
                if limite_inferior < poblacion < limite_superior:
                    pais_encontrado = True
                    print(fila[0])
                    print(f"Población: {poblacion:,}")
                    print(f"Superficie: {float(fila[2]):,.0f} km^2\n")

    if not pais_encontrado:
        print("No se encontró ningún país dentro del rango.\n")


def filtrar_rango_superficie():
    # Bucle de validacion de entrada para los limites (admite decimales)
    while True:
        try:
            print("Filtrando por superficie:")
            limite_inferior = float(input("Ingrese el límite inferior del rango: "))
            limite_superior = float(input("Ingrese el límite superior del rango: "))

            if limite_inferior < 0 or limite_superior < 0:
                print("Inválido - los límites no pueden ser menores a 0.")
                print()
            elif limite_superior < limite_inferior:
                print("Inválido - el límite superior no puede ser menor al límite inferior.")
                print()
        except ValueError:
            print("Inválido - los valores deben ser un número entero o decimal.")
            print()
        else:
            break

    pais_encontrado = False
    print()

    with open("paises.csv", "r", newline="", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        next(lector)
        for fila in lector:
            if fila:
                # Comprueba si la superficie (columna 2) esta dentro del rango
                # Nota: convierte la superficie del CSV a int para comparar
                if limite_superior > int(fila[2]) > limite_inferior:
                    pais_encontrado = True
                    print(fila[0])
                    print(f"Población: {int(fila[1]):,}")
                    print(f"Superficie: {float(fila[2]):,.0f} km^2\n") 

    if not pais_encontrado:
        print("No se encontró ningún país dentro del rango.")

def menu_filtrar_paises():
    # Bucle principal del menu
    while True:
        print("===MENÚ===")
        print("Filtrar por:")
        print("    |1| Continente")
        print("    |2| Rango de población")
        print("    |3| Rango de superficie")
        print("    |4| Salir")

        opt = input("\nOpción: ")

        if opt == '1':
            filtrar_por_continente()
        elif opt == '2':
            filtrar_rango_poblacion()
        elif opt == '3':
            filtrar_rango_superficie()
        elif opt == '4':
            break # Regresa al menu principal
        else:
            print("Opción inválida.\n")

def ordenar_paises():
    paises = []

    try:
        # Lee los datos del CSV a una lista de diccionarios
        with open("paises.csv", newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                try:
                    # Procesa y limpia cada fila antes de agregarla
                    paises.append({
                        "nombre": fila.get("nombre", "").strip(),
                        "poblacion": int(float(fila.get("poblacion", 0))),
                        "superficie": float(fila.get("superficie", 0)),
                        "continente": fila.get("continente", "").strip().capitalize()
                    })
                except (ValueError, TypeError):
                    continue # Omite filas mal formadas
    except FileNotFoundError:
        print("No se encontró el archivo paises.csv.")
        return

    if not paises:
        print("No hay datos para ordenar.")
        return

    # Menu de criterios de ordenamiento
    print("=== ORDENAR PAÍSES ===")
    print("    |1| Ordenar por nombre")
    print("    |2| Ordenar por población")
    print("    |3| Ordenar por superficie\n")

    opt = input("Opción: ").strip()
    print()

    if opt not in ("1", "2", "3"):
        print("Opción inválida.")
        return

    # Seleccion de direccion (Ascendente/Descendente)
    orden = input("    (A) Ascendente / (D) Descendente: ").strip().upper()
    print()

    if orden not in ("A", "D"):
        print("Opción inválida.")
        return

    descendente = (orden == "D") # Booleano para el parametro 'reverse'

    # Aplica el ordenamiento usando 'sort' y una funcion lambda 'key'
    if opt == '1':
        # Ordena alfabeticamente ignorando mayusculas
        paises.sort(key=lambda p: p["nombre"].lower() if p["nombre"] else "", reverse=descendente)
    elif opt == '2':
        # Ordena numericamente por poblacion
        paises.sort(key=lambda p: p["poblacion"], reverse=descendente)
    elif opt == '3':
        # Ordena numericamente por superficie
        paises.sort(key=lambda p: p["superficie"], reverse=descendente)

    print()
    print("=== RESULTADO ORDENADO ==")
    print()

    # Imprime la lista ordenada con formato
    for pais in paises:
        # Usa .get() para manejar datos potencialmente faltantes
        nombre = pais.get("nombre") or "Desconocido"
        poblacion = pais.get("poblacion") or 0
        superficie = pais.get("superficie") or 0
        continente = pais.get("continente") or "Desconocido"

        print(nombre)
        print(f"    Población: {poblacion:,}")
        print(f"    Superficie: {superficie:,.0f} km^2")
        print(f"    Continente: {continente}\n")

def mostrar_estadisticas():
    paises = [] # Lista para almacenar los datos leidos

    try:
        # Lee el archivo usando DictReader para facilitar el acceso por nombre de columna
        with open("paises.csv", newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                try:
                    # Convierte y almacena los datos de cada fila
                    paises.append({
                        "nombre": fila.get("nombre", "").strip(),
                        "poblacion": int(float(fila.get("poblacion", 0))),
                        "superficie": float(fila.get("superficie", 0)),
                        "continente": fila.get("continente", "").strip().capitalize()
                    })
                except (ValueError, TypeError):
                    # Omite filas con datos numericos invalidos
                    continue
    except FileNotFoundError:
        print("No se encontró el archivo paises.csv.")
        return

    # Comprueba si se cargaron datos
    if not paises:
        print("No hay datos para analizar.")
        return

    # Calculos estadisticos
    pais_mayor = max(paises, key=lambda p: p["poblacion"])
    pais_menor = min(paises, key=lambda p: p["poblacion"])

    prom_pob = sum(p["poblacion"] for p in paises) / len(paises)
    prom_sup = sum(p["superficie"] for p in paises) / len(paises)

    # Conteo de paises por continente
    continentes = {}
    for p in paises:
        c = p["continente"] or "Desconocido" # Agrupa continentes vacios
        continentes[c] = continentes.get(c, 0) + 1

    # Muestra los resultados
    print("=== ESTADÍSTICAS ===")
    print(f"    Mayor población: {pais_mayor['nombre']} ({pais_mayor['poblacion']:,} habitantes)")
    print(f"    Menor población: {pais_menor['nombre']} ({pais_menor['poblacion']:,} habitantes)")
    print(f"    Promedio de población: {prom_pob:,.0f} habitantes")
    print(f"    Promedio de superficie: {prom_sup:,.0f} km^2\n")

    print("Cantidad de países por continente:")
    for continente, cantidad in sorted(continentes.items()):
        print(f"    {continente}: {cantidad}\n")
