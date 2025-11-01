#estadisticas

def mostrar_estadisiticas(paises):

    if not paises:
        print("No se encuentran paises cargados")
        return
    
    print("------ ESTADÍSTICAS ---------")

    pais_mayor_poblacion = max(paises, key=lambda p: p['poblacion'])
    #pais con menor población
    pais_menor_poblacion = min(paises, key=lambda p: p['poblacion'])

    #promedio
    total_pob = sum(p['poblacion'] for p in paises)
    promedio_pob = total_pob / len(paises)

    #promedio superficie
    total_superficie = sum(p['superficie'] for p in paises)
    promedio_sup = total_superficie / len(paises)

    #cantida de paises por continente
    continentes = {}
    for p in paises:
        cont = p['continente'].strip().capitalize()
        continentes[cont] = continentes.get(cont, 0) + 1

    #resultados
    print(f"Pais con mayor población: {pais_mayor_poblacion['nombre']} ({pais_mayor_poblacion['poblacion']:,} habitantes)")
    print(f"pais con menor población: {pais_menor_poblacion['nombre']} ({pais_menor_poblacion['poblacion']:,})")
    print(f"promedio de población: {promedio_pob:,.0f} habitantes")
    print(f"promedio de superficie: {promedio_sup:,.0f} km2")

    print("cantidad de paises por continente: ")
    for cont, cantidad in continentes.items():
        print(f" - {cont}: {cantidad}")
        
        print()

