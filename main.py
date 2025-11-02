if __name__ == '__main__':
    import funciones

    print("=== MENÚ ===")
    print("    |1| Buscar un país")
    print("    |2| Filtrar países")
    print("    |3| Ordenar países")
    print("    |4| Mostrar estadísticas")
    print("    |5| Salir\n")

    opt = input("Opción: ")
    print()

    while True:
        if opt == '1':
            funciones.buscar_pais()
        elif opt == '2':
            funciones.menu_filtrar_paises()
        elif opt == '3':
            funciones.ordenar_paises()
        elif opt == '4':
            funciones.mostrar_estadisticas()
        elif opt == '5':
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")