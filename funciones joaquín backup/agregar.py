import csv

def agregar_pais():
    print("=== AGREGAR NUEVO PAÍS ===")
    #ingresar el nombre, población. superficie y continente del pais agregado
    nombre = input("Nombre del país: ").strip()
    poblacion = input("Población: ").strip()
    superficie = input("Superficie (km²): ").strip()
    continente = input("Continente: ").strip().capitalize()
#en caso de faltar una opción
    if not (nombre and poblacion and superficie and continente):
        print("Todos los campos son obligatorios.")
        return
#en caso de agregar un valor inválido en población y superficie
    try:
        poblacion = int(float(poblacion))
        superficie = float(superficie)
    except ValueError:
        print("Población o superficie inválidas.")
        return

    # Escribir en el CSV
    with open("paises.csv", "a", newline='', encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([nombre, poblacion, superficie, continente])

    print(f"{nombre} fue agregado al archivo")