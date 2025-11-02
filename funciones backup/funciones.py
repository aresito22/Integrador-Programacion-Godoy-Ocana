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
                    print(f"Población: {fila[1]:,}")
                    print(f"Superficie: {fila[2]:,.0f} km^2\n")
                elif pais_buscar in (fila[0]).lower():
                    pais_encontrado = True
                    print(fila[0])
                    print(f"Población: {fila[1]:,}")
                    print(f"Superficie: {fila[2]:,.0f} km^2\n")

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
                print(f"Población: {fila[1]:,}")
                print(f"Superficie: {fila[2]:,.0f} km^2\n")

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
                    print(f"Población: {fila[1]:,}")
                    print(f"Superficie: {fila[2]:,.0f} km^2\n") 

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

def agregar_pais():
    print("=== AGREGAR NUEVO PAÍS ===")

    nombre = input("Nombre del país: ").strip().capitalize()
    poblacion = input("Población: ").strip()
    superficie = input("Superficie (km^2): ").strip()
    continente = input("Continente: ").strip().capitalize()

    print()

    if not (nombre and poblacion and superficie and continente):
        print("Inválido - todos los campos son obligatorios.")
        print()
        return

    try:
        poblacion = int(float(poblacion))
        superficie = float(superficie)
    except ValueError:
        print("Población o superficie inválidas.")
        print()
        return

    with open("paises.csv", "a", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([nombre, poblacion, superficie, continente])

    print(f"{nombre} fue agregado correctamente.\n")

def mostrar_estadisticas():
    paises = []

    try:
        with open("paises.csv", newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                try:
                    paises.append({
                        "nombre": fila.get("nombre", "").strip(),
                        "poblacion": int(float(fila.get("poblacion", 0))),
                        "superficie": float(fila.get("superficie", 0)),
                        "continente": fila.get("continente", "").strip().capitalize()
                    })
                except (ValueError, TypeError):
                    continue
    except FileNotFoundError:
        print("No se encontró el archivo paises.csv.")
        print()
        return

    if not paises:
        print("No hay datos para analizar.")
        print()
        return

    pais_mayor = max(paises, key=lambda p: p["poblacion"])
    pais_menor = min(paises, key=lambda p: p["poblacion"])

    prom_pob = sum(p["poblacion"] for p in paises) / len(paises)
    prom_sup = sum(p["superficie"] for p in paises) / len(paises)

    continentes = {}
    for p in paises:
        c = p["continente"] or "Desconocido"
        continentes[c] = continentes.get(c, 0) + 1

    print("=== ESTADÍSTICAS ===")
    print(f"Mayor población: {pais_mayor['nombre']} ({pais_mayor['poblacion']:,} habitantes)")
    print(f"Menor población: {pais_menor['nombre']} ({pais_menor['poblacion']:,} habitantes)")
    print(f"Promedio de población: {prom_pob:,.0f} habitantes")
    print(f"Promedio de superficie: {prom_sup:,.0f} km^2\n")

    print("Cantidad de países por continente:")
    for continente, cantidad in sorted(continentes.items()):
        print(f"    {continente}: {cantidad}")

def ordenar_paises():
    paises = []

    try:
        with open("paises.csv", newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                try:
                    paises.append({
                        "nombre": fila.get("nombre", "").strip(),
                        "poblacion": int(float(fila.get("poblacion", 0))),
                        "superficie": float(fila.get("superficie", 0)),
                        "continente": fila.get("continente", "").strip().capitalize()
                    })
                except (ValueError, TypeError):
                    continue
    except FileNotFoundError:
        print("No se encontró el archivo paises.csv.\n")
        return

    if not paises:
        print("No hay datos para ordenar.\n")
        return

    print("=== ORDENAR PAÍSES ===")
    print("    |1| Ordenar por nombre")
    print("    |2| Ordenar por población")
    print("    |3| Ordenar por superficie\n")

    opt = input("Opción: ").strip()
    print()

    if opt not in ("1", "2", "3"):
        print("Opción inválida.")
        print()
        return

    orden = input("    (A) Ascendente / (D) Descendente: ").strip().upper()
    if orden not in ("A", "D"):
        print("Opción inválida.\n")
        return

    descendente = (orden == "D")

    if opt == '1':
        paises.sort(key=lambda p: p["nombre"].lower() if p["nombre"] else "", reverse=descendente)
    elif opt == '2':
        paises.sort(key=lambda p: p["poblacion"], reverse=descendente)
    elif opt == '3':
        paises.sort(key=lambda p: p["superficie"], reverse=descendente)

    print("=== RESULTADO ORDENADO ==\n")

    for pais in paises:
        nombre = pais.get("nombre") or "Desconocido"
        poblacion = pais.get("poblacion") or 0
        superficie = pais.get("superficie") or 0
        continente = pais.get("continente") or "Desconocido"

        print(nombre)
        print(f"Población: {poblacion:,}")
        print(f"Superficie: {superficie:,.0f} km^2")
        print(f"Continente: {continente}\n")