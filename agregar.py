#agregar

def agregar_pais(paises):

    print("-------------- AGREGAR NUEVO PAÍS ----------------")

    #ingreso de nombre
    nombre = input("ingrese el nombre del país: ").strip().capitalize()
    if not nombre:
        print("El nombre no puede estar vacío")
        return
    
    #verificar existencia
    for p in paises:
        if p['nombre'].lower() == nombre.lower():
            print("Ese pais ya existe en la lista")
            return
        
    #población 
    try:
        poblacion = int(input("ingrese la población total: "))
        if poblacion <= 0:
            print("la población debe ser un numero positivo")
            return
    except ValueError:
        print("debe ingresar un número válido para la población")
        return
    
    #superficie
    try:
        superficie = float(input("ingrese la superficie en km: "))
        if superficie <= 0:
            print("ingrese un numero positivo")
            return
    except ValueError:
        print("debe ingresar un numero valido")
        return
    
    #ingreso del continente
    continente = input("Ingrese el continente: ").strip().capitalize()
    if continente not in ["America", "Africa", "Asia", "Europa", "Oceanía"]:
        print("Ingrese un continente existente")
        return
    
    #ingreso del nuevo pais

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente,
    }

    #agregar a la lista
    paises.append(nuevo_pais)
    print(f"{nombre} fue agregado a la lista")

    #cuantos paises hay en total
    print(f"total de paises en la lista: {len(paises)}\n")

    return paises

    