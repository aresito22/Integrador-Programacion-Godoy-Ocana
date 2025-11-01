#ordenar paises

def ordenar_paises(paises):
    if not paises:
        print("no se encuentran paises")
        return
    
    #menú
    print("------------- ORDENAR PAISES -------------")
    print("1) Por nombre")
    print("2) por población")
    print("3) Por superficie")

    opciones = input("Seleccione una opción: ")

    if opciones not in ["1", "2", "3"]:
        print("opción invalida")
        return
    
    orden = input("Ingrese (A) para que el orden sea ascendente o (D) para que sea descendente").strip().upper()
    if orden not in ["A", "D"]:
        print("opción invalida")
        return
    
    #opción para habilitar el descendiente
    descendiente = True if orden == "D" else False

#el formato de la lista según opción
    if opciones == "1":
        paises_ordenados = sorted(paises, key=lambda p: p['nombre'].lower(), reverse=descendiente)
    elif opciones == "2":
        paises_ordenados = sorted(paises, key=lambda p: p['poblacion'], reverse=descendiente)
    elif opciones == "3":
        paises_ordenados = sorted(paises, key=lambda p: p['superficie'], reverse=descendiente)
        
#interfaz de la lista
    print("lista ordenada: ")
    for p in paises_ordenados:
        print(f"{p['nombre']} - {p['poblacion']} habitantes - {p['superficie']} km2 - {p['continente']}")

