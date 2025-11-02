import csv

def ordenar_paises():
    paises = []
    try:
        with open("paises.csv", newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                paises.append({
                    "nombre": fila["nombre"].strip(),
                    "poblacion": int(float(fila["poblacion"])),
                    "superficie": float(fila["superficie"]),
                    "continente": fila["continente"].strip().capitalize()
                })
    except FileNotFoundError:
        print("No se encontró el archivo paises.csv.")
        return

    if not paises:
        print("El archivo está vacío.")
        return

    print("=== ORDENAR PAÍSES ===")
    print("1. Por nombre")
    print("2. Por población")
    print("3. Por superficie")

    opcion = input("Seleccione una opción (1-3): ").strip()
    if opcion not in ["1", "2", "3"]:
        print("Opción inválida.")
        return

    orden = input("¿Ascendente (A) o descendente (D)? ").strip().upper()
    descendente = True if orden == "D" else False

    if opcion == "1":
        paises.sort(key=lambda p: p["nombre"].lower(), reverse=descendente)
    elif opcion == "2":
        paises.sort(key=lambda p: p["poblacion"], reverse=descendente)
    elif opcion == "3":
        paises.sort(key=lambda p: p["superficie"], reverse=descendente)

    print("=== RESULTADO ORDENADO ===")
    for p in paises:
        print(f"{p['nombre']} - {p['poblacion']} hab - {p['superficie']} km² - {p['continente']}")