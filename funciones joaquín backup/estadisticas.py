import csv

def mostrar_estadisticas():
    #llamado al csv
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
        print("No hay países cargados.")
        return
#para ver cual es el pais con mayor y menor poblacion
    pais_mayor = max(paises, key=lambda p: p["poblacion"])
    pais_menor = min(paises, key=lambda p: p["poblacion"])
#para ver cual es el promedio por poblacion y superficie
    prom_pob = sum(p["poblacion"] for p in paises) / len(paises)
    prom_sup = sum(p["superficie"] for p in paises) / len(paises)
#para saber la cantidad de paises por continente
    continentes = {}
    for p in paises:
        cont = p["continente"]
        continentes[cont] = continentes.get(cont, 0) + 1
#interfaz
    print("=== ESTADÍSTICAS ===")
    print(f"Mayor población: {pais_mayor['nombre']} ({pais_mayor['poblacion']:,})")
    print(f"Menor población: {pais_menor['nombre']} ({pais_menor['poblacion']:,})")
    print(f"Promedio población: {prom_pob:,.0f}")
    print(f"Promedio superficie: {prom_sup:,.0f}\n")

    print("Cantidad de países por continente:")
    for cont, cant in continentes.items():
        print(f"   {cont}: {cant}")